from src.market_data import MarketData
from src.volatility import HistoricalVolatility
from src.black_scholes import BlackScholes


market = MarketData(
    "AAPL",
    "2025-01-01",
    "2026-01-01"
)


prices = market.get_prices()


# Latest stock price
S0 = float(
    prices.iloc[-1]
)


# Historical volatility
volatility = HistoricalVolatility(
    prices
)

sigma = volatility.annualized()


# Assume ATM option
option = BlackScholes(
    S0,
    S0,
    30/365,
    0.05,
    sigma
)


print(
    "Stock price:",
    S0
)

print(
    "Historical volatility:",
    sigma
)

print(
    "Call price:",
    option.call_price()
)

print(
    "Put price:",
    option.put_price()
)