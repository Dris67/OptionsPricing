import pytest
import numpy as np

from src.black_scholes import BlackScholes
from src.finite_difference import FiniteDifference


# Test 1 : Compare with Black Scholes

def test_black_scholes_comparison():

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

    bs_price = bs.call_price()
    fd_price = fd.explicit_call()

    assert abs(bs_price - fd_price) < 0.05
# --------------------------------------------------------


# Test 2 : Grid Convergence

def test_grid_convergence():

    bs = BlackScholes(
        100,
        100,
        1,
        0.05,
        0.2
    )

    true_price = bs.call_price()

    grids = [
        (25, 1000),
        (50, 2000),
        (75, 3000),
        (100, 5000),
    ]

    errors = []

    for M, N in grids:

        fd = FiniteDifference(
            100,
            100,
            1,
            0.05,
            0.2,
            M=M,
            N=N
        )

        price = fd.explicit_call()

        errors.append(abs(price - true_price))

    # Final grid should be the most accurate
    assert errors[-1] == min(errors)
# --------------------------------------------------------


# Test 3 : Multiple Parameter Sets

def test_multiple_parameter_sets():

    test_cases = [

        (100, 100, 1.0, 0.05, 0.20),

        (120, 100, 1.0, 0.05, 0.20),

        (80, 100, 1.0, 0.05, 0.20),

        (100, 110, 0.5, 0.03, 0.25),

        (100, 90, 2.0, 0.04, 0.30),

    ]

    tolerance = 0.10

    for S, K, T, r, sigma in test_cases:

        bs = BlackScholes(
            S,
            K,
            T,
            r,
            sigma
        )

        fd = FiniteDifference(
            S,
            K,
            T,
            r,
            sigma,
            M=100,
            N=5000
        )

        assert abs(
            bs.call_price()
            -
            fd.explicit_call()
        ) < tolerance
# --------------------------------------------------------


# Test 4 : Numerical Sanity Checks

def test_numerical_sanity():

    fd = FiniteDifference(
        100,
        100,
        1,
        0.05,
        0.2,
        M=100,
        N=5000
    )

    price = fd.explicit_call()

    assert np.isfinite(price)

    assert price > 0

    assert price < 100
# --------------------------------------------------------


# Test 5 : Stability Check

def test_unstable_grid():

    with pytest.raises(ValueError):

        fd = FiniteDifference(
            100,
            100,
            1,
            0.05,
            0.2,
            M=300,
            N=300
        )

        fd.explicit_call()
# --------------------------------------------------------


# Test 6 : Invalid Inputs

@pytest.mark.parametrize(
    "S,K,T,r,sigma",
    [
        (-100, 100, 1, 0.05, 0.2),
        (100, -100, 1, 0.05, 0.2),
        (100, 100, -1, 0.05, 0.2),
        (100, 100, 1, 0.05, -0.2),
    ]
)
def test_invalid_inputs(S, K, T, r, sigma):

    with pytest.raises(ValueError):

        FiniteDifference(
            S,
            K,
            T,
            r,
            sigma
        )