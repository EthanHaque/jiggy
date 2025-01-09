"""Jiggy commaands for managing the Minecraft server."""

import logging
import re
import subprocess

import discord
from discord import app_commands
from discord.ext import commands


class MinecraftCog(
    commands.GroupCog, name="minecraft", description="Minecraft server commands"
):
    """Collection of commands for the Minecraft server."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @app_commands.command()
    async def whitelist(self, inter: discord.Interaction, username: str):
        """Whitelist a user on the Minecraft server.

        Parameters
        ----------
        interaction : discord.Interaction
            discord.py event interaction object.
        username : str
            Minecraft username to whitelist on the server.
        """
        self.logger.info(
            "%s called whitelist from guild %d in channel %d",
            inter.user,
            inter.guild_id,
            inter.channel_id,
        )
        tmux_session = "minecraft"

        if not minecraft_username_is_valid(username):
            await inter.response.send_message("The provided username is invalid.")
        else:
            sanitized_minecraft_username = sanitize_minecraft_username(username)
            send_tmux_command(
                tmux_session, f"whitelist add {sanitized_minecraft_username}"
            )
            self.logger.info("Added %s to the whitelist", sanitize_minecraft_username)
            await inter.response.send_message(
                f"Added {sanitized_minecraft_username} to the whitelist"
            )


def minecraft_username_is_valid(username: str) -> bool:
    """Check if a username is a valid Minecraft username.

    A Minecraft username must be 3-16 characters long inclusive. Must only
    contain alphanumeric characters (i.e. only a-z A-Z 0-9) or underscores
    (_).

    Parameters
    ----------
    username : str
        Minecraft username to check against rules.
    """
    pattern = re.compile(r"^[a-zA-Z0-9_]{3,16}$")
    return pattern.match(username)


def sanitize_minecraft_username(username: str) -> str:
    """Remove disallowed characters from a user supplied Minecraft username.

    A Minecraft username must be 3-16 characters long inclusive. Must only
    contain alphanumeric characters (i.e. only a-z A-Z 0-9) or underscores
    (_).

    Parameters
    ----------
    username : str
        Minecraft username to sanitize.
    """
    cleaned = re.sub(r"[^a-zA-Z0-9_]", "", username)
    return cleaned[:16]


def send_tmux_command(session_name: str, command: str):
    """Send a command to a tmux session.

    Parameters
    ----------
    session_name : str
        Identifier for the tmux session.
    command : str
        Sends this string to the tmux session and runs it.
    """
    logger = logging.getLogger(__name__)
    try:
        args = ["tmux", "send-keys", "-t", f"{session_name}:0", command, "ENTER"]
        # subprocess.run( args, check=True)
        logger.debug("called " + " ".join(args))
    except subprocess.CalledProcessError as e:
        # TODO: use builtin logging functionality for printing errors
        logger.error(
            f"Failed to send tmux command '{command}' to session '{session_name}': {e}"
        )


async def setup(bot: commands.Bot) -> None:
    """Set up cog."""
    logger = logging.getLogger(__name__)
    logger.debug("Extension %s loaded.", __name__)
    await bot.add_cog(MinecraftCog(bot))


async def teardown(bot: commands.Bot) -> None:
    """Unload cog."""
    _ = bot
    logger = logging.getLogger(__name__)
    logger.debug("Extension %s unloaded.", __name__)
