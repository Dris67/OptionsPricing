from src.black_scholes import BlackScholes

option = BlackScholes(
    S=100,
    K=100,
    T=1,
    r=0.05,
    sigma=0.2
)

print("Black-Scholes Pricing")
print("----------------------")
print(f"Call Price : {option.call_price():.4f}")
print(f"Put Price  : {option.put_price():.4f}")

print()

print("Greeks")
print("-------")
print(f"Call Delta : {option.delta('call'):.4f}")
print(f"Put Delta  : {option.delta('put'):.4f}")
print(f"Gamma      : {option.gamma():.4f}")
print(f"Vega       : {option.vega():.4f}")
print(f"Call Theta : {option.theta('call'):.4f}")
print(f"Put Theta  : {option.theta('put'):.4f}")
print(f"Call Rho   : {option.rho('call'):.4f}")
print(f"Put Rho    : {option.rho('put'):.4f}")