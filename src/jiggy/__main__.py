import os
import pathlib

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.none()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)


@bot.event
async def setup_hook():
    for file in pathlib.Path("src/jiggy/extensions/").rglob("*.py"):
        if file.stem.startswith("_"):
            continue
        await bot.load_extension(".".join(file.with_suffix("").parts[1:]))
    await bot.tree.sync()  # This function is used to sync the slash commands with Discord it is mandatory if you want to use slash commands


bot.setup_hook = setup_hook


@bot.event
async def on_ready() -> None:  # This event is called when the bot is ready
    print(f"Logged in as {bot.user}")


@bot.tree.command()
async def ping(inter: discord.Interaction) -> None:
    await inter.response.send_message(f"> Pong! {round(bot.latency * 1000)}ms")


bot.run(TOKEN)
