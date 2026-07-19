from src.market_data import MarketData
from src.volatility import HistoricalVolatility
from src.mc_simulator import StockSimulator
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


ticker = "AAPL"


# Get last 1 year data

end = datetime.today()

start = end - timedelta(days=365)


market = MarketData(
    ticker,
    start.strftime("%Y-%m-%d"),
    end.strftime("%Y-%m-%d")
)


prices = market.get_prices()


# Current stock price

S0 = float(
    prices.iloc[-1]
)


# Historical volatility

vol = HistoricalVolatility(
    prices
)

sigma = vol.annualized()



# Simulate next 1 year

simulator = StockSimulator(

    S0=S0,

    r=0.05,

    sigma=sigma,

    T=1,

    steps=252,

    paths=100
)


paths = simulator.simulate()

mean_path = np.mean(
    paths,
    axis=0
)


upper = np.percentile(
    paths,
    95,
    axis=0
)


lower = np.percentile(
    paths,
    5,
    axis=0
)

# Plot
plt.figure(figsize=(12,5))


# Plot some sample paths
for path in paths[:50]:
    plt.plot(path)


# Expected path
plt.plot(
    mean_path,
    linewidth=2,
    label="Expected Path"
)


# Confidence interval
plt.fill_between(
    range(len(mean_path)),
    lower,
    upper,
    alpha=0.3,
    label="90% Confidence Range"
)


plt.title(
    f"{ticker} Monte Carlo Future Price Simulation"
)

plt.xlabel(
    "Trading Days"
)

plt.ylabel(
    "Stock Price ($)"
)


plt.legend()

plt.grid(True)

plt.show()