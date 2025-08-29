# MkDocs Chatbot Plugin

<div align="center">
<br>
<img src="assets/logo.png" alt="PDM logo" width="250">
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
    pip install your-package
    ```

Add the plugin to your `mkdocs.yaml` configuration:
```yaml
plugins:
    - chatbot:
        url: <your_chat_url>
```
