import numpy as np
from src.monte_carlo import MonteCarlo


def test_call():

    np.random.seed(42)

    option = MonteCarlo(
        100,
        100,
        1,
        0.05,
        0.2,
        500000
    )

    assert abs(
        option.price("call")
        -
        10.4506
    ) < 0.10


def test_put():

    np.random.seed(42)

    option = MonteCarlo(
        100,
        100,
        1,
        0.05,
        0.2,
        500000
    )

    assert abs(
        option.price("put")
        -
        5.5735
    ) < 0.10