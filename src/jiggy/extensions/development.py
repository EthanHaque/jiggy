"""Jiggy commaands for working on Jiggy."""

import logging

import discord
from discord import app_commands
from discord.ext import commands


class DevelopmentCog(commands.Cog):
    """Collection of commands for use in development."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @app_commands.command()
    async def sync(self, inter: discord.Interaction):
        """Sync all commands globally to discord.

        Must be called when a command interface is updated, added, or removed
        so that Discord knows the proper interface to show to the user. Otherwise,
        can take up to an hour for update to appear.
        """
        self.logger.info(
            "%s called sync from guild %d in channel %d",
            inter.user,
            inter.guild_id,
            inter.channel_id,
        )
        synced = await self.bot.tree.sync()
        await inter.response.send_message(f"Synced {len(synced)} commands globally")


async def setup(bot: commands.Bot) -> None:
    """Set up cog."""
    logger = logging.getLogger(__name__)
    logger.debug("Extension %s loaded.", __name__)
    await bot.add_cog(DevelopmentCog(bot))


async def teardown(bot: commands.Bot) -> None:
    """Unload cog."""
    _ = bot
    logger = logging.getLogger(__name__)
    logger.debug("Extension %s unloaded.", __name__)
