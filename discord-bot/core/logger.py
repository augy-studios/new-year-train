import discord

async def log_action(bot, message, log_guild_id, log_channel_id):
    guild = bot.get_guild(log_guild_id)
    if guild is None:
        print("Log guild not found.")
        return

    log_channel = guild.get_channel(log_channel_id)
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
        attachment_links = "\n".join(attachment.url for attachment in message.attachments)
        embed.add_field(name="Attachments", value=attachment_links, inline=False)

    await log_channel.send(embed=embed)
