from src.binomial import BinomialTree


def test_call():

    option = BinomialTree(
        100,
        100,
        1,
        0.05,
        0.2,
        500
    )

    assert abs(option.price("call") - 10.4506) < 0.02


def test_put():

    option = BinomialTree(
        100,
        100,
        1,
        0.05,
        0.2,
        500
    )

    assert abs(option.price("put") - 5.5735) < 0.02