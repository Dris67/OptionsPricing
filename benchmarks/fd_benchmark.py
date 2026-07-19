import time

from src.black_scholes import BlackScholes
from src.finite_difference import FiniteDifference


def benchmark():

    print("=" * 78)
    print("Finite Difference Benchmark")
    print("=" * 78)

    bs = BlackScholes(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2
    )

    bs_price = bs.call_price()

    print(f"\nBlack-Scholes Price : {bs_price:.6f}\n")

    print(
        f"{'M':>6}"
        f"{'N':>8}"
        f"{'FD Price':>16}"
        f"{'Error':>16}"
        f"{'Time (s)':>16}"
    )

    print("-" * 78)

    grids = [

        (25, 1000),

        (50, 2000),

        (75, 3000),

        (100, 5000),

    ]

    previous_error = None

    for M, N in grids:

        fd = FiniteDifference(
            S0=100,
            K=100,
            T=1,
            r=0.05,
            sigma=0.2,
            M=M,
            N=N
        )

        start = time.perf_counter()

        price = fd.explicit_call()

        end = time.perf_counter()

        runtime = end - start

        error = abs(price - bs_price)

        print(
            f"{M:6d}"
            f"{N:8d}"
            f"{price:16.6f}"
            f"{error:16.6f}"
            f"{runtime:16.6f}"
        )

        if previous_error is not None:

            if error < previous_error:
                print("   ✓ Error decreased")

            else:
                print("   ✗ Error increased")

        previous_error = error

    print("\nBenchmark completed.")


if __name__ == "__main__":
    benchmark()