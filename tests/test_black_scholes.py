from src.black_scholes import BlackScholes


def test_call_price():
    option = BlackScholes(100, 100, 1, 0.05, 0.20)
    assert abs(option.call_price() - 10.4506) < 0.001


def test_put_price():
    option = BlackScholes(100, 100, 1, 0.05, 0.20)
    assert abs(option.put_price() - 5.5735) < 0.001