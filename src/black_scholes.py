import numpy as np
from scipy.stats import norm


class BlackScholes:
    """
    Black-Scholes model for pricing European call and put options.
    """

    def __init__(self, S, K, T, r, sigma):
        if S <= 0:
            raise ValueError("Stock price must be positive.")

        if K <= 0:
            raise ValueError("Strike price must be positive.")

        if T <= 0:
            raise ValueError("Time to maturity must be positive.")

        if sigma <= 0:
            raise ValueError("Volatility must be positive.")
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
    
    def delta(self, option_type="call"):
        d1 = self.d1()

        if option_type == "call":
            return norm.cdf(d1)
        elif option_type == "put":
            return norm.cdf(d1) - 1
        else:
            raise ValueError("option_type must be 'call' or 'put'")
        
    def gamma(self):
        d1 = self.d1()

        return (
            norm.pdf(d1)
            /
            (self.S * self.sigma * np.sqrt(self.T))
        )
    
    def vega(self):
        d1 = self.d1()

        return (
            self.S
            * norm.pdf(d1)
            * np.sqrt(self.T)
        ) /100 # Vega expressed per 1% change in volatility
    
    def theta(self, option_type="call"):
        d1 = self.d1()
        d2 = self.d2()

        first_term = (
            -self.S
            * norm.pdf(d1)
            * self.sigma
            /
            (2 * np.sqrt(self.T))
        )

        if option_type == "call":
            second_term = (
                -self.r
                * self.K
                * np.exp(-self.r * self.T)
                * norm.cdf(d2)
            )

        elif option_type == "put":
            second_term = (
                self.r
                * self.K
                * np.exp(-self.r * self.T)
                * norm.cdf(-d2)
            )

        else:
            raise ValueError("option_type must be 'call' or 'put'")

        return first_term + second_term
    
    def rho(self, option_type="call"):
        d2 = self.d2()

        if option_type == "call":
            return (
                self.K
                * self.T
                * np.exp(-self.r * self.T)
                * norm.cdf(d2)
            )

        elif option_type == "put":
            return (
                -self.K
                * self.T
                * np.exp(-self.r * self.T)
                * norm.cdf(-d2)
            )

        else:
            raise ValueError("option_type must be 'call' or 'put'")