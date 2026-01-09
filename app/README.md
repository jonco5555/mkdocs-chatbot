# MkDocs Chatbot App

A Streamlit-based chatbot application that provides an interactive AI-powered interface to chat with the mkdocs-chatbot plugin documentation.

## Overview

This application uses LlamaIndex and Google GenAI to create a conversational interface that allows users to ask questions about the mkdocs-chatbot plugin and receive intelligent, context-aware answers based on the documentation.

## Features

- 🤖 AI-powered Q&A using Google GenAI
- 📚 Vector-based document retrieval from markdown files
- 💬 Interactive chat interface built with Streamlit
- 🔍 Context-aware responses based on plugin documentation

## Requirements

- Python >=3.12, <4.0
- Google GenAI API key
- Streamlit account (for deployment) or local Streamlit installation

## Installation

1. Install dependencies:
```bash
uv sync
```

Or with pip:
```bash
pip install -e .
```

## Configuration

The app requires the following secrets to be configured in Streamlit:

- `GOOGLE_API_KEY`: Your Google GenAI API key
- `GOOGLE_LLM_MODEL`: The Google GenAI LLM model to use (e.g., "gemini-pro")
- `GOOGLE_EMB_MODEL`: The Google GenAI embedding model to use (e.g., "models/embedding-001")

### Setting up Streamlit Secrets

For local development, create a `.streamlit/secrets.toml` file in your project root:

```toml
GOOGLE_API_KEY = "your-api-key-here"
GOOGLE_LLM_MODEL = "gemini-pro"
GOOGLE_EMB_MODEL = "models/embedding-001"
```

For Streamlit Cloud deployment, configure these secrets in your app settings.

## Running the App

### Local Development

```bash
streamlit run main.py
```

The app will be available at `http://localhost:8501`

### Streamlit Cloud

Deploy the app to Streamlit Cloud by connecting your GitHub repository and configuring the secrets in the app settings.

## How It Works

1. **Document Loading**: The app loads all markdown files from the `docs/` directory
2. **Indexing**: Documents are processed and indexed into a vector store using Google GenAI embeddings
3. **Chat Interface**: Users can ask questions through the Streamlit chat interface
4. **Query Processing**: Questions are processed using the vector index to find relevant documentation
5. **Response Generation**: The LLM generates context-aware answers based on the retrieved documentation
