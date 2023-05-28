import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

DB_ID = os.getenv("DB_ID")
DB_API_KEY = os.getenv("DB_API_KEY")
WEATHER_API_KEY= os.getenv("WEATHER_API_KEY")