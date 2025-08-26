import os
from pathlib import Path

from jinja2 import Environment
from mkdocs.config import config_options
from mkdocs.config.base import Config
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.utils import write_file


class ChatbotConfig(Config):
    url = config_options.Type(str)


class ChatbotPlugin(BasePlugin[ChatbotConfig]):
    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        # Add the overrides directory to the theme configuration
        overrides_path = Path(__file__).resolve().parent / "overrides"
        config.theme.dirs.insert(0, str(overrides_path))
        return config

    def on_env(
        self, env: Environment, /, *, config: MkDocsConfig, files: Files
    ) -> Environment:
        # Add custom CSS to the site
        css_filename = "assets/chatbot.css"
        css_content = Path(__file__).resolve().parent.joinpath(css_filename).read_text()
        write_file(css_content.encode(), os.path.join(config.site_dir, css_filename))
        config.extra_css.insert(0, css_filename)

        # Add the chatbot URL to the Jinja2 environment
        env.globals.setdefault("chatbot_url", self.config.url)
        return env
