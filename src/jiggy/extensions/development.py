import logging
import discord
from discord import app_commands
from discord.ext import commands


class DevelopmentCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    async def sync(self, inter: discord.Interaction):
        synced = await self.bot.tree.sync()
        await inter.response.send_message(f"Synced {len(synced)} commands globally")


async def setup(bot):
    await bot.add_cog(DevelopmentCog(bot))


async def teardown(bot):
    logger = logging.getLogger(__name__)
    logger.info("Extension unloaded.")
