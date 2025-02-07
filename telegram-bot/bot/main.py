import asyncio
from telethon import TelegramClient, events

from .config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL_ID
from .logger import log_event
from .commands import handle_command

import requests

def set_bot_commands():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setMyCommands"

    commands = [
        {"command": "start", "description": "Start the bot"},
        {"command": "help", "description": "Show help information"},
        {"command": "ping", "description": "Check bot latency"},
        {"command": "dm", "description": "Send a private message to another user (Owner only)"},
        {"command": "broadcast", "description": "Send a message to all users who interacted with the bot (Owner only)"}
    ]

    response = requests.post(url, json={"commands": commands})
    
    if response.status_code == 200:
        print("Bot commands set successfully!")
    else:
        print(f"Failed to set commands: {response.text}")

# Call the function to set commands when the bot starts
if __name__ == "__main__":
    set_bot_commands()

class NewYearTrainBot:
    def __init__(self, api_id, api_hash, bot_token, log_channel_id):
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.log_channel_id = log_channel_id
        
        # Create the client using the bot token
        self.client = TelegramClient("NewYearTrainBotSession", self.api_id, self.api_hash).start(bot_token=self.bot_token)
    
    def run(self):
        # Register event handler for new messages
        @self.client.on(events.NewMessage)
        async def message_handler(event):
            # 1) Store the user's ID if not already recorded
            await self.store_user_id(event.sender_id)
            
            # 2) Log the event
            await log_event(event, self.client, self.log_channel_id)
            
            # 3) Check if it's a command (starts with "/")
            message_text = event.raw_text
            if message_text.startswith("/"):
                # Grab the command (strip out the "/" and any arguments)
                command = message_text.split()[0][1:].lower()
                await handle_command(command, event, self.client)
        
        print("NewYearTrain Bot is now running...")
        self.client.run_until_disconnected()

    async def store_user_id(self, user_id):
        """
        Store user ID in a file if it's not already there.
        """
        try:
            with open("users.txt", "r") as f:
                users = {int(line.strip()) for line in f}
        except FileNotFoundError:
            users = set()

        if user_id not in users:
            with open("users.txt", "a") as f:
                f.write(f"{user_id}\n")
                print(f"Added user {user_id} to the broadcast list.")

if __name__ == "__main__":
    bot = NewYearTrainBot(API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL_ID)
    bot.run()
