
## Example Implementation

Under the `app` folder, you'll find a simple Streamlit application that demonstrates how to build a compatible backend:

### Features

- Uses `llama-index` for document embedding and retrieval
- Integrates with Google Gemini for LLM responses
- Loads documentation from your `docs/` directory
- Provides a chat interface optimized for iframe embedding

### Setup Instructions

1. **Install dependencies**:
   ```bash
   cd app
   uv sync  # or pip install -r requirements.txt
   ```

2. **Configure API keys**:
   - The example uses Google Gemini API
   - Set your API key in `app/main.py` (or use environment variables for production)
   - You'll need:
     - Google Gemini API key for the LLM
     - Google Gemini API key for embeddings

3. **Configure the documentation path**:
   - Update `DATA_PATH` in `app/main.py` to point to your documentation directory
   - By default, it points to `../docs/` relative to the app directory

4. **Run the Streamlit app**:
   ```bash
   streamlit run app/main.py
   ```
   The app will typically run on `http://localhost:8501`

5. **Configure MkDocs**:
   ```yaml
   plugins:
       - chatbot:
           url: "http://localhost:8501"  # or your production URL
   ```

### Building Your Own Backend

You're not limited to the Streamlit example. You can build your backend using any framework (Flask, FastAPI, Django, etc.) as long as it:

- Serves a web page that can be embedded in an iframe
- Provides a chat interface (can be simple HTML/JavaScript or a full framework)
- Connects to an embedding service and LLM API
- Processes your documentation files for semantic search

The backend can be:
- **Hosted separately** - Deploy your chat backend independently (e.g., on a cloud service)
- **Co-located with MkDocs** - Run both services on the same server
- **Multi-tenant** - Support multiple documentation projects using the `project` query parameter
