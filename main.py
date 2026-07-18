from src.black_scholes import BlackScholes


def main():
    option = BlackScholes(
        S=100,
        K=100,
        T=1.0,
        r=0.05,
        sigma=0.20,
    )

    print(f"Call Price : {option.call_price():.4f}")
    print(f"Put Price  : {option.put_price():.4f}")


if __name__ == "__main__":
    main()