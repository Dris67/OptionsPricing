import time

from src.black_scholes import BlackScholes
from src.binomial import BinomialTree
from src.monte_carlo import MonteCarlo


S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2


def benchmark_black_scholes():
    bs = BlackScholes(S, K, T, r, sigma)

    start = time.perf_counter()
    bs.call_price()
    end = time.perf_counter()

    return end - start


def benchmark_binomial():
    bt = BinomialTree(S, K, T, r, sigma, 1000)

    start = time.perf_counter()
    bt.price("call")
    end = time.perf_counter()

    return end - start


def benchmark_monte_carlo():
    mc = MonteCarlo(S, K, T, r, sigma, 100000)

    start = time.perf_counter()
    mc.price("call")
    end = time.perf_counter()

    return end - start


print("Runtime (seconds)")
print("-----------------")
print(f"Black-Scholes : {benchmark_black_scholes():.8f}")
print(f"Binomial Tree : {benchmark_binomial():.8f}")
print(f"Monte Carlo   : {benchmark_monte_carlo():.8f}")