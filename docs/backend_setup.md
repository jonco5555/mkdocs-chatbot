## Backend Requirements

The `mkdocs-chatbot` plugin provides the frontend interface (the chatbot button and iframe) that appears in your MkDocs documentation. However, to make the chatbot functional, you need to set up a **separate backend chat application** that:

1. **Embeds your documentation** - Processes your Markdown files and creates vector embeddings for semantic search
2. **Provides a chat interface** - Serves a web-based chat UI that can be embedded in an iframe
3. **Connects to an LLM** - Uses a language model (like Google Gemini, OpenAI GPT, etc.) to generate responses based on your documentation

## Interface Requirements

The backend chat application must:

- **Be accessible via URL** - The plugin loads the chat interface in an iframe, so your backend must be accessible at a URL (e.g., `http://localhost:8501` for local development or `https://your-chat-app.com` for production)
- **Support iframe embedding** - The chat interface should be designed to work within an iframe (typically 400px wide)
- **Accept a project parameter** (optional) - The plugin automatically appends `?project=<project_name>` to the URL, which can be used to support multiple documentation projects from a single backend
