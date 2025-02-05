import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from core.logger import setup_error_handling

# Load token from token.env
load_dotenv("token.env")
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("Missing DISCORD_TOKEN in token.env")

# Define bot with command prefix
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent if needed
bot = commands.Bot(command_prefix="!", intents=intents)

# Function to update the activity
async def update_activity():
    num_guilds = len(bot.guilds)
    activity = discord.Activity(type=discord.ActivityType.watching, name=f"over {num_guilds} servers")
    await bot.change_presence(activity=activity)

# Load cogs
async def load_cogs():
    await bot.load_extension("bot.commands.general")
    await bot.load_extension("bot.commands.moderation")
    await bot.load_extension("bot.commands.info")

# Register slash commands
@bot.event
async def on_ready():
    await load_cogs()
    await bot.tree.sync()  # Sync commands with Discord
    await update_activity()  # Update the status on startup
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

# Update activity whenever the bot joins a new guild
@bot.event
async def on_guild_join(guild):
    await update_activity()

# Update activity whenever the bot leaves a guild
@bot.event
async def on_guild_remove(guild):
    await update_activity()

# Initialize error handling
setup_error_handling(bot)

# Run the bot
bot.run(TOKEN)