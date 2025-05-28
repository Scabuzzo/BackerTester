from alpaca_trade_api.rest import REST, TimeFrame
from dotenv import load_dotenv
import os
import pandas as pd

# Load .env file
load_dotenv()

# Get keys from environment
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

api = REST(API_KEY, API_SECRET, BASE_URL)

# Fetch historical data
bars = api.get_bars("AAPL", TimeFrame.Day, limit=100).df
print(bars.head())
