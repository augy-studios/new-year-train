import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load token from token.env
load_dotenv("token.env")
TOKEN = os.getenv("DISCORD_TOKEN")
LOG_GUILD_ID = int(os.getenv("LOG_GUILD_ID"))
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))

if not TOKEN:
    raise ValueError("Missing DISCORD_TOKEN in token.env")

# Define bot with command prefix
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent if needed
bot = commands.Bot(command_prefix="!", intents=intents)

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
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

async def log_action(bot, message):
    guild = bot.get_guild(LOG_GUILD_ID)
    if guild is None:
        print("Log guild not found.")
        return

    log_channel = guild.get_channel(LOG_CHANNEL_ID)
    if log_channel is None:
        print("Log channel not found.")
        return

    embed = discord.Embed(
        title="Message Log",
        description=f"[Message Link](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})",
        color=discord.Color('#66ff66'),
    )
    embed.add_field(name="Author", value=f"{message.author} (ID: {message.author.id})", inline=True)
    embed.add_field(name="Server", value=f"{message.guild.name} (ID: {message.guild.id})", inline=True)
    embed.add_field(name="Channel", value=f"{message.channel.name} (ID: {message.channel.id})", inline=True)
    embed.add_field(name="Content", value=message.content or "No content", inline=False)
    
    if message.attachments:
        attachments = "\n".join([attachment.url for attachment in message.attachments])
        embed.add_field(name="Attachments", value=attachments, inline=False)

    await log_channel.send(embed=embed)

# Run the bot
bot.run(TOKEN)