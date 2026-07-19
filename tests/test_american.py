import pytest

from src.binomial import BinomialTree
from src.black_scholes import BlackScholes

# Test 1: European Binomial converges to Black-Scholes

def test_european_call_matches_black_scholes():

    bs = BlackScholes(
        100,
        100,
        1,
        0.05,
        0.2
    )

    tree = BinomialTree(
        100,
        100,
        1,
        0.05,
        0.2,
        steps=500
    )

    binomial_price = tree.price(
        option_type="call",
        american=False
    )

    bs_price = bs.call_price()

    assert abs(
        binomial_price - bs_price
    ) < 0.05
# --------------------------------------------------


# Test 2: American call = European call
# (for non-dividend paying stocks)

def test_american_call_matches_european_call():

    tree = BinomialTree(
        100,
        100,
        1,
        0.05,
        0.2,
        steps=500
    )

    european_call = tree.price(
        option_type="call",
        american=False
    )

    american_call = tree.price(
        option_type="call",
        american=True
    )

    assert abs(
        american_call - european_call
    ) < 0.05
# --------------------------------------------------


# Test 3: American put should be more valuable

def test_american_put_greater_than_european_put():

    tree = BinomialTree(
        100,
        100,
        1,
        0.05,
        0.2,
        steps=500
    )

    european_put = tree.price(
        option_type="put",
        american=False
    )

    american_put = tree.price(
        option_type="put",
        american=True
    )

    assert american_put >= european_put
# --------------------------------------------------


# Test 4: Option price should be positive

@pytest.mark.parametrize(
    "option_type",
    [
        "call",
        "put"
    ]
)
def test_option_price_positive(option_type):

    tree = BinomialTree(
        100,
        100,
        1,
        0.05,
        0.2,
        steps=200
    )

    price = tree.price(
        option_type=option_type,
        american=True
    )

    assert price > 0
# --------------------------------------------------


# Test 5: Invalid option type

def test_invalid_option_type():

    tree = BinomialTree(
        100,
        100,
        1,
        0.05,
        0.2,
        steps=100
    )

    with pytest.raises(ValueError):

        tree.price(
            option_type="invalid",
            american=True
        )
# --------------------------------------------------


# Test 6: Convergence with increasing steps

def test_binomial_convergence():

    prices = []

    steps_list = [
        50,
        100,
        250,
        500
    ]

    for steps in steps_list:

        tree = BinomialTree(
            100,
            100,
            1,
            0.05,
            0.2,
            steps=steps
        )

        price = tree.price(
            option_type="call",
            american=False
        )

        prices.append(price)


    bs = BlackScholes(
        100,
        100,
        1,
        0.05,
        0.2
    )

    error_initial = abs(
        prices[0] - bs.call_price()
    )

    error_final = abs(
        prices[-1] - bs.call_price()
    )


    assert error_final < error_initial