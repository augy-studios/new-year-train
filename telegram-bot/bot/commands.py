import time

async def handle_command(command: str, event, client):
    """
    Handle commands based on the command text (e.g. 'start', 'ping', 'help', etc.).
    """
    if command == "start":
        await command_start(event, client)
    elif command == "help":
        await command_help(event, client)
    elif command == "ping":
        await command_ping(event, client)
    else:
        await event.reply("Unknown command. Try /help")

async def command_start(event, client):
    """
    Example /start command.
    """
    await event.reply("Hello! I am NewYearTrain Bot. Type /help to see what I can do.")

async def command_help(event, client):
    """
    Example /help command.
    """
    help_text = (
        "Available Commands:\n"
        "/start - Greet the user.\n"
        "/help - Show this help message.\n"
        "/ping - Check the bot's latency.\n"
        # Add more commands as you see fit
    )
    await event.reply(help_text)

async def command_ping(event, client):
    """
    Example /ping command to check latency (ping).
    A simple approach is to note the current time, reply, and measure round-trip time.
    """
    start_time = time.time()
    message = await event.reply("Pong!")
    end_time = time.time()
    
    # The difference is how long it took to send & get a confirmation from Telegram
    latency_ms = (end_time - start_time) * 1000
    await message.edit(f"Pong! Latency: {latency_ms:.2f} ms")
