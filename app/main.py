"""
PDM Documentation Chatbot using LlamaIndex with Gemini models.

Requirements:
pip install streamlit
pip install llama-index
pip install llama-index-llms-gemini
pip install llama-index-embeddings-gemini
pip install google-generativeai
"""

import os
import streamlit as st
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
import google.generativeai as genai

# Page configuration
st.set_page_config(
    page_title="Chat with the PDM docs",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("Chat with the PDM docs 💬🦙")
st.info(
    "PDM - A modern Python package and dependency manager. "
    "Check out the full documentation at [PDM docs](https://pdm-project.org).",
    icon="📃",
)

# Configure Gemini API
# You can set the API key either through Streamlit secrets or environment variable
GOOGLE_API_KEY = st.secrets.get("google_api_key", os.getenv("GOOGLE_API_KEY"))

if not GOOGLE_API_KEY:
    st.error(
        "Please set your Google API key in Streamlit secrets or as an environment variable."
    )
    st.stop()

# Configure Gemini models
genai.configure(api_key=GOOGLE_API_KEY)

# Set up Gemini Flash 2.0 for chat
Settings.llm = Gemini(
    model="gemini-2.0-flash-exp",  # Using Gemini 2.0 Flash
    api_key=GOOGLE_API_KEY,
    temperature=0.5,
    system_prompt="You are an expert on PDM and your job is to answer technical questions. "
    "Assume that all questions are related to PDM. Keep your answers technical and based on facts - do not hallucinate features.",
)

# Set up Gemini embeddings
Settings.embed_model = GeminiEmbedding(
    model_name="models/text-embedding-004",  # Latest Gemini embedding model
    api_key=GOOGLE_API_KEY,
    title="PDM Documentation Embeddings",
)

# Data path configuration
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs/")

# Initialize chat messages history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me a question about PDM!",
        }
    ]


@st.cache_resource(show_spinner=False)
def load_data():
    """Load and index PDM documentation."""
    with st.spinner(
        text="Loading and indexing the PDM docs - hang tight! This should take 1-2 minutes."
    ):
        try:
            # Check if documents directory exists
            if not os.path.exists(DATA_PATH):
                st.error(f"Documents directory not found at {DATA_PATH}")
                st.stop()

            # Load documents
            reader = SimpleDirectoryReader(
                input_dir=DATA_PATH, recursive=True, required_exts=[".md"]
            )
            docs = reader.load_data()

            if not docs:
                st.warning("No markdown files found in the documents directory.")
                st.stop()

            # Create index with Gemini embeddings
            index = VectorStoreIndex.from_documents(docs, show_progress=True)

            return index

        except Exception as e:
            st.error(f"Error loading documents: {str(e)}")
            st.stop()


# Load the index
index = load_data()

# Initialize the chat engine
if "chat_engine" not in st.session_state.keys():
    st.session_state.chat_engine = index.as_chat_engine(
        chat_mode="condense_question",
        verbose=True,
        similarity_top_k=3,  # Number of similar chunks to retrieve
    )

# Chat interface
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Generate response if last message is from user
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message)
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
