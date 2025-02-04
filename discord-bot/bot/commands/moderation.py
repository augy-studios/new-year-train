import discord
from discord.ext import commands
from discord import app_commands
from core.logger import log_action

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Kick a user.")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"User {member.name} kicked for reason: {reason}")
        await log_action(self.bot, interaction)

    @app_commands.command(name="ban", description="Ban a user.")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"User {member.name} banned for reason: {reason}")
        await log_action(self.bot, interaction)

    @app_commands.command(name="mute", description="Mute a user.")
    async def mute(self, interaction: discord.Interaction, member: discord.Member, duration: int):
        # Custom mute logic here (add roles or restrict channel permissions)
        await interaction.response.send_message(f"User {member.name} muted for {duration} minutes.")
        await log_action(self.bot, interaction)

async def setup(bot):
    await bot.add_cog(Moderation(bot))