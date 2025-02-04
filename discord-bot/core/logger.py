import os
import discord
from dotenv import load_dotenv

# Load environment variables from token.env
load_dotenv("token.env")
LOG_GUILD_ID = int(os.getenv("LOG_GUILD_ID"))
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))

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
        title="New Message Logged",
        description=f"[Message Link](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})",
        color=discord.Color.blue(),
    )
    embed.add_field(name="Author", value=f"{message.author} (ID: {message.author.id})", inline=True)
    embed.add_field(name="Server", value=f"{message.guild.name} (ID: {message.guild.id})", inline=True)
    embed.add_field(name="Channel", value=f"{message.channel.name} (ID: {message.channel.id})", inline=True)
    embed.add_field(name="Content", value=message.content or "No content", inline=False)
    
    if message.attachments:
        attachments = "\n".join([attachment.url for attachment in message.attachments])
        embed.add_field(name="Attachments", value=attachments, inline=False)

    await log_channel.send(embed=embed)