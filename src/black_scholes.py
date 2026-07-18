import numpy as np
from scipy.stats import norm


class BlackScholes:
    """
    Black-Scholes model for pricing European call and put options.
    """

    def __init__(self, S, K, T, r, sigma):
        self.S = float(S)
        self.K = float(K)
        self.T = float(T)
        self.r = float(r)
        self.sigma = float(sigma)

    def d1(self):
        numerator = (
            np.log(self.S / self.K)
            + (self.r + 0.5 * self.sigma**2) * self.T
        )

        denominator = self.sigma * np.sqrt(self.T)

        return numerator / denominator

    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)

    def call_price(self):
        d1 = self.d1()
        d2 = self.d2()

        return (
            self.S * norm.cdf(d1)
            - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        )

    def put_price(self):
        d1 = self.d1()
        d2 = self.d2()

        return (
            self.K * np.exp(-self.r * self.T) * norm.cdf(-d2)
            - self.S * norm.cdf(-d1)
        )