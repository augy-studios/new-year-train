import discord
from discord.ext import commands
from discord import app_commands
from core.logger import log_action

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check the bot's latency.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! 🏓 Latency: {latency}ms")
        await log_action(self.bot, interaction)

async def setup(bot):
    await bot.add_cog(General(bot))
