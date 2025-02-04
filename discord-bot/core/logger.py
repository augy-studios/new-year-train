import os
import discord
from dotenv import load_dotenv

# Load environment variables from token.env
load_dotenv("token.env")
LOG_GUILD_ID = int(os.getenv("LOG_GUILD_ID"))
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))

async def log_action(bot, interaction):
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
        description=f"Command: {interaction.command.name} | [Message Link](https://discord.com/channels/{interaction.guild.id}/{interaction.channel.id}/{interaction.id})",
        color=discord.Color(0x99ff99),
    )
    embed.add_field(name="User", value=f"{interaction.user} (ID: {interaction.user.id})", inline=True)
    embed.add_field(name="Server", value=f"{interaction.guild.name} (ID: {interaction.guild.id})", inline=True)
    embed.add_field(name="Channel", value=f"{interaction.channel.name} (ID: {interaction.channel.id})", inline=True)

    await log_channel.send(embed=embed)