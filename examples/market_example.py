from src.market_data import MarketData


market = MarketData(
    "AAPL",
    "2025-01-01",
    "2026-01-01"
)


prices = market.get_prices()

print(prices.head())
print(prices.tail())