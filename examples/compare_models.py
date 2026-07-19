from src.black_scholes import BlackScholes
from src.binomial import BinomialTree
from src.monte_carlo import MonteCarlo

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

bs = BlackScholes(S, K, T, r, sigma)
bt = BinomialTree(S, K, T, r, sigma, steps=500)
mc = MonteCarlo(S, K, T, r, sigma, simulations=100000)

print("=" * 60)
print("OPTION PRICING COMPARISON")
print("=" * 60)

print(f"{'Method':<20}{'Call Price':>15}{'Put Price':>15}")
print("-" * 50)

print(f"{'Black-Scholes':<20}{bs.call_price():>15.4f}{bs.put_price():>15.4f}")
print(f"{'Binomial Tree':<20}{bt.price('call'):>15.4f}{bt.price('put'):>15.4f}")
print(f"{'Monte Carlo':<20}{mc.price('call'):>15.4f}{mc.price('put'):>15.4f}")