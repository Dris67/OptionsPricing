import matplotlib.pyplot as plt

from src.black_scholes import BlackScholes
from src.monte_carlo import MonteCarlo

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

bs = BlackScholes(S, K, T, r, sigma)
true_price = bs.call_price()

simulations = [
    100,
    500,
    1000,
    5000,
    10000,
    50000,
    100000,
]

errors = []

for n in simulations:
    mc = MonteCarlo(S, K, T, r, sigma, n)
    price = mc.price("call")
    errors.append(abs(price - true_price))

plt.figure(figsize=(8, 5))
plt.plot(simulations, errors, marker="o")

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Number of Simulations")
plt.ylabel("Absolute Error")

plt.title("Monte Carlo Error")

plt.grid(True)

plt.savefig("figures/mc_error.png")

plt.show()