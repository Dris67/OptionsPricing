import numpy as np

class HistoricalVolatility:


    def __init__(
        self,
        prices
    ):

        self.prices = prices


    def returns(self):

        return np.log(
            self.prices /
            self.prices.shift(1)
        ).dropna()


    def annualized(self):

        daily_returns = self.returns()

        daily_vol = np.std(
            daily_returns
        )

        annual_vol = (
            daily_vol *
            np.sqrt(252)
        )

        return float(annual_vol)