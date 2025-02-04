import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load token from token.env
load_dotenv("token.env")
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("Missing DISCORD_TOKEN in token.env")

# Define bot with command prefix
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent if needed
bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs
async def load_cogs():
    await bot.load_extension("bot.commands.ping")

# Register slash commands
@bot.event
async def on_ready():
    await load_cogs()
    await bot.tree.sync()  # Sync commands with Discord
    print(f"Logged in as {bot.user}")

# Run the bot
bot.run(TOKEN)