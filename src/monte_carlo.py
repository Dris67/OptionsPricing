import numpy as np


class MonteCarlo:

    def __init__(self, S, K, T, r, sigma, simulations):

        if S <= 0:
            raise ValueError("Stock price must be positive.")

        if K <= 0:
            raise ValueError("Strike price must be positive.")

        if T <= 0:
            raise ValueError("Time to maturity must be positive.")

        if sigma <= 0:
            raise ValueError("Volatility must be positive.")

        if simulations <= 0:
            raise ValueError("Number of simulations must be positive.")

        self.S = float(S)
        self.K = float(K)
        self.T = float(T)
        self.r = float(r)
        self.sigma = float(sigma)
        self.simulations = int(simulations)

    def simulate_terminal_prices(self):

        Z = np.random.standard_normal(self.simulations)

        return self.S * np.exp(
            (self.r - 0.5 * self.sigma**2) * self.T
            +
            self.sigma * np.sqrt(self.T) * Z
        )
    
    def price(self, option_type="call"):

        ST = self.simulate_terminal_prices()

        if option_type == "call":
            payoff = np.maximum(ST - self.K, 0)

        elif option_type == "put":
            payoff = np.maximum(self.K - ST, 0)

        else:
            raise ValueError(
                "option_type must be 'call' or 'put'"
            )

        return np.exp(-self.r * self.T) * np.mean(payoff)
    
    def confidence_interval(self, option_type="call"):

        ST = self.simulate_terminal_prices()

        if option_type == "call":
            payoff = np.maximum(ST-self.K,0)

        else:
            payoff = np.maximum(self.K-ST,0)

        discounted = np.exp(-self.r*self.T)*payoff

        mean = np.mean(discounted)

        std = np.std(discounted,ddof=1)

        margin = 1.96*std/np.sqrt(self.simulations)

        return (
            mean,
            mean-margin,
            mean+margin
        )