import yfinance as yf


class MarketData:

    def __init__(
        self,
        ticker,
        start,
        end
    ):

        self.ticker = ticker
        self.start = start
        self.end = end


    def get_prices(self):

        data = yf.download(
            self.ticker,
            start=self.start,
            end=self.end,
            auto_adjust=False
        )

        if data.empty:
            raise ValueError(
                "No market data found."
            )


        # Extract closing prices
        prices = data["Close"]


        # Convert DataFrame with one column
        # into a Series
        prices = prices.squeeze()


        return prices