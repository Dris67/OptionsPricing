import numpy as np


class FiniteDifference:

    def __init__(
        self,
        S0,
        K,
        T,
        r,
        sigma,
        M=100,
        N=5000,
        S_max=None,
    ):

        if S0 <= 0:
            raise ValueError("Stock price must be positive.")

        if K <= 0:
            raise ValueError("Strike price must be positive.")

        if T <= 0:
            raise ValueError("Time to maturity must be positive.")

        if sigma <= 0:
            raise ValueError("Volatility must be positive.")

        self.S0 = float(S0)
        self.K = float(K)
        self.T = float(T)
        self.r = float(r)
        self.sigma = float(sigma)

        self.M = int(M)
        self.N = int(N)

        self.S_max = 3 * K if S_max is None else float(S_max)

        self.dS = self.S_max / self.M
        self.dt = self.T / self.N

        self.S = np.linspace(0, self.S_max, self.M + 1)

    def _check_stability(self):

        limit = 1.0 / (self.sigma ** 2 * self.M ** 2)

        if self.dt > limit:

            raise ValueError(
                f"""
    Explicit scheme unstable.

    Current dt = {self.dt}

    Maximum dt = {limit}

    Increase N.
    """
            )
        
    def explicit_call(self):

        self._check_stability()

        V = np.zeros((self.M + 1, self.N + 1))

        # Terminal condition
        V[:, -1] = np.maximum(self.S - self.K, 0)

        # Boundary conditions
        time = np.linspace(0, self.T, self.N + 1)

        V[0, :] = 0.0

        V[-1, :] = (
            self.S_max
            - self.K * np.exp(-self.r * (self.T - time))
        )

        # Step backwards in time
        for j in range(self.N - 1, -1, -1):

            for i in range(1, self.M):

                alpha = 0.5 * self.dt * (
                    self.sigma ** 2 * i ** 2
                    - self.r * i
                )

                beta = (
                    1
                    - self.dt * (
                        self.sigma ** 2 * i ** 2
                        + self.r
                    )
                )

                gamma = 0.5 * self.dt * (
                    self.sigma ** 2 * i ** 2
                    + self.r * i
                )

                V[i, j] = (
                    alpha * V[i - 1, j + 1]
                    + beta * V[i, j + 1]
                    + gamma * V[i + 1, j + 1]
                )

        return float(
            np.interp(
                self.S0,
                self.S,
                V[:, 0]
            )
        )