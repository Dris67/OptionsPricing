from src.black_scholes import BlackScholes
from src.binomial import BinomialTree
from src.monte_carlo import MonteCarlo


def main():

    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2

    bs = BlackScholes(S, K, T, r, sigma)

    bt = BinomialTree(
        S,
        K,
        T,
        r,
        sigma,
        500
    )

    mc = MonteCarlo(
        S,
        K,
        T,
        r,
        sigma,
        100000
    )

    print("="*60)
    print("OPTION PRICING COMPARISON")
    print("="*60)

    print(f"{'Method':<20}{'Call':>12}{'Put':>12}")

    print("-"*44)

    print(
        f"{'Black-Scholes':<20}"
        f"{bs.call_price():>12.4f}"
        f"{bs.put_price():>12.4f}"
    )

    print(
        f"{'Binomial Tree':<20}"
        f"{bt.price('call'):>12.4f}"
        f"{bt.price('put'):>12.4f}"
    )

    print(
        f"{'Monte Carlo':<20}"
        f"{mc.price('call'):>12.4f}"
        f"{mc.price('put'):>12.4f}"
    )

if __name__ == "__main__":
    main()