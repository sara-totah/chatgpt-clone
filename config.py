import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if API key is available
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please check your .env file.")

# Model configuration
MODEL_NAME = "gpt-3.5-turbo"

# Database configuration
DB_PATH = "conversations.json" 