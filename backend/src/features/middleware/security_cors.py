import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read the string and split it by commas into a Python list
# Fallback to local defaults if the .env variable is missing
raw_origins = os.getenv(
    "ALLOWED_ORIGINS", 
    "http://localhost:3000,http://localhost:5173"
)

CORS_ORIGINS = [origin.strip() for origin in raw_origins.split(",")]