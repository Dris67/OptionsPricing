from src.binomial import BinomialTree

option = BinomialTree(
    S=100,
    K=100,
    T=1,
    r=0.05,
    sigma=0.2,
    steps=500
)

print("Binomial Tree Pricing")
print("----------------------")
print(f"Call Price : {option.price('call'):.4f}")
print(f"Put Price  : {option.price('put'):.4f}")