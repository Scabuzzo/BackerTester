# main.py
from data import get_stock_data
from logger import setup_logger

logger = setup_logger()

def main():
    logger.info("Starting backtest")

    df = get_stock_data()
    logger.info("Data fetched successfully")
    logger.debug(f"\n{df.head()}")

if __name__ == "__main__":
    main()
    logger.info("Script executed successfully")
