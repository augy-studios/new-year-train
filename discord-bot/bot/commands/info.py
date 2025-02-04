from discord.ext import commands
from discord import app_commands
import discord
import platform
from core.logger import log_action

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="userinfo", description="Get user information.")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(title="User Info", color=discord.Color.green())
        embed.add_field(name="Username", value=member.name, inline=False)
        embed.add_field(name="User ID", value=member.id, inline=False)
        embed.add_field(name="Joined", value=member.joined_at, inline=False)
        await interaction.response.send_message(embed=embed)
        await log_action(self.bot, interaction)

    @app_commands.command(name="botinfo", description="Get bot information.")
    async def botinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Bot Info", color=discord.Color.purple())
        embed.add_field(name="Bot Name", value=self.bot.user.name)
        embed.add_field(name="Python Version", value=platform.python_version())
        embed.add_field(name="Library", value="discord.py")
        await interaction.response.send_message(embed=embed)
        await log_action(self.bot, interaction)

    @app_commands.command(name="serverinfo", description="Get server information.")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(title="Server Info", color=discord.Color.orange())
        embed.add_field(name="Server Name", value=guild.name)
        embed.add_field(name="Server ID", value=guild.id)
        embed.add_field(name="Member Count", value=guild.member_count)
        await interaction.response.send_message(embed=embed)
        await log_action(self.bot, interaction)

async def setup(bot):
    await bot.add_cog(Info(bot))
