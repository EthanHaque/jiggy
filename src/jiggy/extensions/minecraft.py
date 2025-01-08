import logging
import discord
from discord import app_commands
from discord.ext import commands


class MinecraftCog(
    commands.GroupCog, name="minecraft", description="Minecraft server commands"
):
    @app_commands.command()
    async def whitelist(self, inter: discord.Interaction):
        await inter.reponse.send_message("test")


async def setup(bot):
    await bot.add_cog(MinecraftCog(bot))


async def teardown(bot):
    logger = logging.getLogger(__name__)
    logger.info("Extension unloaded.")
