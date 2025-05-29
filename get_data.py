from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from datetime import datetime
from dotenv import load_dotenv
import os
import pandas as pd

# Load .env file
load_dotenv()

# Get keys from environment
client = StockHistoricalDataClient(os.getenv("ALPACA_API_KEY"), os.getenv("ALPACA_SECRET_KEY"))

#Request historical data
request_params = StockBarsRequest(
    symbol_or_symbols="AAPL",
    timeframe=TimeFrame.Day,
    start=datetime(2025, 5, 19),
    end=datetime(2025, 5, 23),
    limit=100
)

# Fetch historical data
bars = client.get_stock_bars(request_params).df

# Convert to DataFrame
df = pd.DataFrame(bars)
print(df.head())