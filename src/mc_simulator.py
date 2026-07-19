import numpy as np


class StockSimulator:

    def __init__(
        self,
        S0,
        r,
        sigma,
        T,
        steps=252,
        paths=100
    ):

        if S0 <= 0:
            raise ValueError(
                "Stock price must be positive."
            )

        if sigma <= 0:
            raise ValueError(
                "Volatility must be positive."
            )

        if T <= 0:
            raise ValueError(
                "Time must be positive."
            )

        self.S0 = float(S0)
        self.r = float(r)
        self.sigma = float(sigma)
        self.T = float(T)

        self.steps = steps
        self.paths = paths

        self.dt = T / steps


    def simulate(self):

        prices = np.zeros(
            (
                self.paths,
                self.steps + 1
            )
        )


        prices[:, 0] = self.S0


        for t in range(1, self.steps + 1):

            Z = np.random.standard_normal(
                self.paths
            )


            prices[:, t] = (
                prices[:, t-1]
                *
                np.exp(
                    (
                        self.r
                        -
                        0.5 * self.sigma**2
                    )
                    *
                    self.dt
                    +
                    self.sigma
                    *
                    np.sqrt(self.dt)
                    *
                    Z
                )
            )


        return prices