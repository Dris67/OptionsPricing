import pytest
from src.black_scholes import BlackScholes


def test_call_price():
    option = BlackScholes(100, 100, 1, 0.05, 0.20)
    assert abs(option.call_price() - 10.4506) < 0.001


def test_put_price():
    option = BlackScholes(100, 100, 1, 0.05, 0.20)
    assert abs(option.put_price() - 5.5735) < 0.001

def test_delta():
    option = BlackScholes(100, 100, 1, 0.05, 0.2)

    assert abs(option.delta("call") - 0.6368) < 1e-3
    assert abs(option.delta("put") + 0.3632) < 1e-3


def test_gamma():
    option = BlackScholes(100, 100, 1, 0.05, 0.2)

    assert abs(option.gamma() - 0.0188) < 1e-3


def test_vega():
    option = BlackScholes(100, 100, 1, 0.05, 0.2)

    assert abs(option.vega() - 0.37524) < 1e-3


def test_theta():
    option = BlackScholes(100, 100, 1, 0.05, 0.2)

    assert abs(option.theta("call") + 6.4140) < 1e-3
    assert abs(option.theta("put") + 1.6579) < 1e-3


def test_rho():
    option = BlackScholes(100, 100, 1, 0.05, 0.2)

    assert abs(option.rho("call") - 53.2325) < 1e-3
    assert abs(option.rho("put") + 41.8905) < 1e-3


def test_invalid_stock_price():
    with pytest.raises(ValueError):
        BlackScholes(-100, 100, 1, 0.05, 0.2)


def test_invalid_strike_price():
    with pytest.raises(ValueError):
        BlackScholes(100, -100, 1, 0.05, 0.2)


def test_invalid_time():
    with pytest.raises(ValueError):
        BlackScholes(100, 100, 0, 0.05, 0.2)


def test_invalid_volatility():
    with pytest.raises(ValueError):
        BlackScholes(100, 100, 1, 0.05, -0.2)