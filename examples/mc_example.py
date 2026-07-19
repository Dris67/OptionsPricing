from src.monte_carlo import MonteCarlo

option = MonteCarlo(
    S=100,
    K=100,
    T=1,
    r=0.05,
    sigma=0.2,
    simulations=100000
)

print("Monte Carlo Pricing")
print("-------------------")
print(f"Call Price : {option.price('call'):.4f}")
print(f"Put Price  : {option.price('put'):.4f}")

mean, lower, upper = option.confidence_interval("call")

print()
print("95% Confidence Interval")
print("-----------------------")
print(f"Estimated Price : {mean:.4f}")
print(f"Lower Bound     : {lower:.4f}")
print(f"Upper Bound     : {upper:.4f}")