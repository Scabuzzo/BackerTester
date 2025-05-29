from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from datetime import datetime
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def get_stock_data():
    client = StockHistoricalDataClient(
        os.getenv("ALPACA_API_KEY"),
        os.getenv("ALPACA_SECRET_KEY")
    )

    request_params = StockBarsRequest(
        symbol_or_symbols="AAPL",
        timeframe=TimeFrame.Day,
        start=datetime(2025, 5, 19),
        end=datetime(2025, 5, 23),
        limit=100
    )

    bars = client.get_stock_bars(request_params).df
    return bars
