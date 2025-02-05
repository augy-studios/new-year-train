import asyncio
from telethon import TelegramClient, events

from .config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL_ID
from .logger import log_event
from .commands import handle_command

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
            # Ignore messages from the logging channel
            if event.chat_id == self.log_channel_id:
                return  # Skip processing this message

            # 1) Log the event
            await log_event(event, self.client, self.log_channel_id)
            
            # 2) Check if it's a command (starts with "/")
            message_text = event.raw_text
            if message_text.startswith("/"):
                # Grab the command (strip out the "/" and any arguments)
                command = message_text.split()[0][1:].lower()
                await handle_command(command, event, self.client)
        
        print("NewYearTrain Bot is now running...")
        self.client.run_until_disconnected()

# If you want to run this module directly (python -m bot.main),
# you can do something like this:
if __name__ == "__main__":
    bot = NewYearTrainBot(API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL_ID)
    bot.run()
