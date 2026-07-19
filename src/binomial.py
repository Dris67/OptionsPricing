import numpy as np


class BinomialTree:

    def __init__(self, S, K, T, r, sigma, steps):

        if S <= 0:
            raise ValueError("Stock price must be positive.")

        if K <= 0:
            raise ValueError("Strike price must be positive.")

        if T <= 0:
            raise ValueError("Time to maturity must be positive.")

        if sigma <= 0:
            raise ValueError("Volatility must be positive.")

        if steps <= 0:
            raise ValueError("Steps must be positive.")

        self.S = float(S)
        self.K = float(K)
        self.T = float(T)
        self.r = float(r)
        self.sigma = float(sigma)
        self.steps = int(steps)

        self.dt = self.T / self.steps

        self.u = np.exp(self.sigma * np.sqrt(self.dt))
        self.d = 1 / self.u

        self.p = (
            np.exp(self.r * self.dt) - self.d
        ) / (
            self.u - self.d
        )

    def price(self, option_type="call", american=False):

        stock_prices = np.array([
            self.S * self.u**j * self.d**(self.steps-j)
            for j in range(self.steps + 1)
        ])

        # Terminal payoff
        if option_type == "call":

            option_values = np.maximum(
                stock_prices - self.K,
                0
            )

        elif option_type == "put":

            option_values = np.maximum(
                self.K - stock_prices,
                0
            )

        else:
            raise ValueError(
                "option_type must be 'call' or 'put'"
            )


        discount = np.exp(-self.r * self.dt)

        # Backward induction
        for step in range(self.steps):

            option_values = discount * (
                self.p * option_values[1:]
                +
                (1-self.p) * option_values[:-1]
            )

            # American early exercise condition
            if american:

                stock_prices = np.array([
                    self.S
                    * self.u**j
                    * self.d**(
                        self.steps-step-1-j
                    )
                    for j in range(self.steps-step)
                ])


                if option_type == "call":

                    exercise_value = np.maximum(
                        stock_prices - self.K,
                        0
                    )


                else:

                    exercise_value = np.maximum(
                        self.K - stock_prices,
                        0
                    )


                option_values = np.maximum(
                    option_values,
                    exercise_value
                )


        return option_values[0]