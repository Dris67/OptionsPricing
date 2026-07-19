import matplotlib.pyplot as plt

from src.black_scholes import BlackScholes
from src.binomial import BinomialTree

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

bs = BlackScholes(S, K, T, r, sigma)
true_price = bs.call_price()

steps = [5, 10, 20, 50, 100, 200, 500, 1000]
errors = []

for n in steps:
    tree = BinomialTree(S, K, T, r, sigma, n)
    price = tree.price("call")
    errors.append(abs(price - true_price))

plt.figure(figsize=(8, 5))
plt.plot(steps, errors, marker="o")

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Number of Steps")
plt.ylabel("Absolute Error")

plt.title("Binomial Tree Error")

plt.grid(True)

plt.savefig("figures/binomial_error.png")

plt.show()