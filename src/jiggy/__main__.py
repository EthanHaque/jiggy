#!/usr/bin/env python3

"""Main entrypoint for Jiggy."""

import json
import logging
import logging.config
import os
import pathlib
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv


class JiggyBot(commands.Bot):
    """Jiggy bot."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        """Call on setup.

        Loads cogs within extensions inside the extensions folder.
        """
        for file in pathlib.Path("src/jiggy/extensions/").rglob("*.py"):
            if file.stem.startswith("_"):
                continue
            extension = ".".join(file.with_suffix("").parts[1:])
            await bot.load_extension(extension)

    async def on_ready(self) -> None:
        """Call when bot is ready to accept commands."""
        logger = logging.getLogger(__name__)
        logger.info("Logged in as %s", bot.user)


def setup_logging(
    default_path="logging.json",
    default_level=logging.INFO,
    log_dir="logs",
    env_key="LOG_CFG",
) -> None:
    """Set up global logging configuration."""
    log_dir_path = Path(log_dir)
    log_dir_path.mkdir(parents=True, exist_ok=True)

    logging_config_path = Path(os.getenv(env_key, default_path))
    if Path.exists(logging_config_path):
        with logging_config_path.open("r") as f:
            config = json.load(f)
        # Update file paths dynamically
        config["handlers"]["info_file_handler"]["filename"] = str(
            log_dir_path / "info.log"
        )
        config["handlers"]["error_file_handler"]["filename"] = str(
            log_dir_path / "errors.log"
        )
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


if __name__ == "__main__":
    load_dotenv()
    setup_logging()

    TOKEN = os.getenv("BOT_TOKEN", "")
    intents = discord.Intents.none()
    intents.message_content = True
    bot = JiggyBot(command_prefix=commands.when_mentioned_or("!"), intents=intents)

    text = r"""
 ▄▄▄██▀▀▀ ██▓  ▄████   ▄████ ▓██   ██▓
   ▒██   ▓██▒ ██▒ ▀█▒ ██▒ ▀█▒ ▒██  ██▓
   ░██   ▒██▒▒██░▄▄▄░▒██░▄▄▄░  ▒██ ██▒
▓██▄██▓  ░██░░▓█  ██▓░▓█  ██▓  ░ ▐██▓▒
 ▓███▒   ░██░░▒▓███▀▒░▒▓███▀▒  ░ ██▒▓▒
 ▒▓▒▒░   ░▓   ░▒   ▒  ░▒   ▒    ██▒▒▒░
 ▒ ░▒░    ▒ ░  ░   ░   ░   ░  ▓██ ░▒░░
 ░ ░ ░    ▒ ░░ ░   ░ ░ ░   ░  ▒ ▒ ░░ ░
 ░   ░    ░        ░       ░  ░ ░    ░
                              ░ ░    ░
    """
    terminal_width = os.get_terminal_size().columns
    centered_text = "\n".join(
        " " * max(0, (terminal_width - len(line)) // 2) + line
        for line in text.splitlines()
    )

    logger = logging.getLogger(__name__)
    logger.info(centered_text)

    bot.run(TOKEN, log_handler=None)
