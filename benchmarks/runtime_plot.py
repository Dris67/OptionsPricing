import time
import matplotlib.pyplot as plt

from src.black_scholes import BlackScholes
from src.binomial import BinomialTree
from src.monte_carlo import MonteCarlo

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

bs = BlackScholes(S, K, T, r, sigma)

start = time.perf_counter()
bs.call_price()
bs_time = time.perf_counter() - start

bt = BinomialTree(S, K, T, r, sigma, 1000)

start = time.perf_counter()
bt.price("call")
bt_time = time.perf_counter() - start

mc = MonteCarlo(S, K, T, r, sigma, 100000)

start = time.perf_counter()
mc.price("call")
mc_time = time.perf_counter() - start

methods = [
    "Black-Scholes",
    "Binomial",
    "Monte Carlo"
]

times = [
    bs_time,
    bt_time,
    mc_time
]

plt.figure(figsize=(8,5))

plt.bar(methods, times)

plt.ylabel("Runtime (seconds)")
plt.title("Runtime Comparison")

plt.savefig("figures/runtime_comparison.png")

plt.show()