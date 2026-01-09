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

## Project Name Detection and URL Construction

The plugin automatically determines the project name and constructs the chatbot URL as follows:

### Project Name Detection

The plugin extracts the project name from the current page URL:

- **Local development** (`localhost` or `127.0.0.1`): The project name is set to `"default"`
- **Production/other hosts**: The project name is extracted from the first path segment of the URL
  - For example, if the documentation is served at `https://docs.example.com/myproject/page1`, the project name will be `"myproject"`
  - If no path segment exists, it defaults to `"default"`

### URL Construction

The plugin constructs the chatbot iframe URL by:

1. Taking the base `chatbot_url` from your configuration
2. Checking if the URL already contains query parameters (by looking for a `?` character)
3. Appending the project parameter:
   - If the URL already has query parameters: `&project=<project_name>`
   - If the URL has no query parameters: `?project=<project_name>`
