# MkDocs Chatbot Plugin

<div align="center">
<br>
<img src="assets/logo.png" alt="mkdocs-chatbot logo" width="250">
</div>

## Overview

Tired of endlessly scrolling through documentation to find what you need?

Mkdocs-chatbot transforms your docs into an interactive, AI-powered chat experience — so you get instant answers, personalized guidance, and a smarter way to explore content. Say goodbye to frustration and hello to effortless discovery!

## Installation

Install the plugin:

=== "uv"

    ```bash
    uv add --group docs mkdocs-chatbot
    ```

=== "pip"

    ```bash
    pip install mkdocs-chatbot
    ```

Add the plugin to your `mkdocs.yaml` configuration:
```yaml
plugins:
    - chatbot:
        url: <your_chat_url>
```

## Quick Start

The plugin requires a **backend chat application** to function. The plugin itself only provides the frontend interface (chatbot button and iframe). You need to:

1. Set up a backend chat service that embeds your documentation and connects to an LLM
2. Configure the `url` parameter to point to your backend service

For detailed information on backend requirements, setup instructions, and how to interface with the plugin, see the [Backend Setup Guide](backend_setup.md).
