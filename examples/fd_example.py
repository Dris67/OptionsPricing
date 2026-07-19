from src.black_scholes import BlackScholes
from src.finite_difference import FiniteDifference

bs = BlackScholes(
    100,
    100,
    1,
    0.05,
    0.2
)

fd = FiniteDifference(
    100,
    100,
    1,
    0.05,
    0.2,
    M=100,
    N=5000
)

print("Black-Scholes :", bs.call_price())
print("Finite Difference :", fd.explicit_call())