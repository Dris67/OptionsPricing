import pandas as pd

from src.volatility import HistoricalVolatility



def test_volatility_positive():

    prices = pd.Series(
        [
            100,
            101,
            103,
            102,
            105
        ]
    )


    vol = HistoricalVolatility(
        prices
    )


    result = vol.annualized()


    assert result > 0