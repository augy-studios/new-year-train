import os
from dotenv import load_dotenv

# Load all variables from token.env
load_dotenv("token.env")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")

# Convert to int if your LOG_CHANNEL_ID is numeric
# If your LOG_CHANNEL_ID is something like -100123456789,
# you can do: LOG_CHANNEL_ID = int(LOG_CHANNEL_ID)
LOG_CHANNEL_ID = int(LOG_CHANNEL_ID) if LOG_CHANNEL_ID else None
