import matplotlib.pyplot as plt

from src.black_scholes import BlackScholes
from src.binomial import BinomialTree


S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

bs = BlackScholes(S, K, T, r, sigma)

bs_price = bs.call_price()

steps = [5, 10, 20, 50, 100, 200, 500, 1000]

prices = []

for n in steps:
    tree = BinomialTree(
        S,
        K,
        T,
        r,
        sigma,
        n
    )

    prices.append(tree.price("call"))

plt.figure(figsize=(8,5))

plt.plot(steps, prices, marker="o", label="Binomial")

plt.axhline(
    bs_price,
    linestyle="--",
    label="Black-Scholes"
)

plt.xscale("log")

plt.xlabel("Number of Steps")
plt.ylabel("Call Price")

plt.title("Binomial Tree Convergence")

plt.legend()

plt.grid(True)

plt.savefig("figures/binomial_convergence.png")

plt.show()