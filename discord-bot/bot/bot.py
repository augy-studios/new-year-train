import discord
from discord.ext import commands
import os

class NewYearTrainBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=None, intents=intents)

    async def setup_hook(self):
        # Load command extensions
        await self.load_extension("bot.commands.general")
        await self.load_extension("bot.commands.moderation")
        await self.load_extension("bot.commands.info")

    async def on_ready(self):
        print(f'Logged in as {self.user.name} (ID: {self.user.id})')

    async def on_interaction(self, interaction: discord.Interaction):
        # Log interactions to another server/channel
        await self.log_interaction(interaction)

    async def log_interaction(self, interaction):
        channel_id = int(os.getenv("LOG_CHANNEL_ID"))
        log_channel = self.get_channel(channel_id)

        embed = discord.Embed(title="Interaction Log", color=discord.Color.blue())
        embed.add_field(name="User", value=f"{interaction.user.name} ({interaction.user.id})", inline=False)
        embed.add_field(name="Server", value=f"{interaction.guild.name} ({interaction.guild.id})", inline=False)
        embed.add_field(name="Channel", value=f"{interaction.channel.name} ({interaction.channel.id})", inline=False)
        embed.add_field(name="Command", value=interaction.data.get("name"), inline=False)
        embed.add_field(name="Message ID", value=interaction.message.id if interaction.message else "N/A", inline=False)

        if log_channel:
            await log_channel.send(embed=embed)
