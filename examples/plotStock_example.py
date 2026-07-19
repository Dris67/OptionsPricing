import argparse
from src.market_data import MarketData
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def main():

    parser = argparse.ArgumentParser(
        description="Plot stock price with moving average"
    )

    parser.add_argument(
        "ticker",
        help="Stock ticker symbol (example: AAPL, NVDA, MSFT)"
    )

    args = parser.parse_args()

    ticker = args.ticker.upper()


    end_date = datetime.today()

    start_date = (
        end_date -
        timedelta(days=365)
    )


    market = MarketData(
        ticker,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d")
    )


    prices = market.get_prices()

    moving_average = prices.rolling(
        window=50
    ).mean()

    plt.figure(figsize=(12,5))

    plt.plot(
        prices.index,
        prices.values,
        label=f"{ticker} Price"
    )


    plt.plot(
        moving_average.index,
        moving_average.values,
        label="50-Day Moving Average"
    )


    plt.xlabel("Date")
    plt.ylabel("Price ($)")

    plt.title(
        f"{ticker} Stock Price - Last 1 Year"
    )


    plt.legend()

    plt.xticks(
        rotation=45
    )

    plt.grid(True)

    plt.tight_layout()

    plt.show()



if __name__ == "__main__":
    main()