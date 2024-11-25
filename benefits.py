import math

class Benefits:
    def __init__(self):
        pass

    def binomial_coefficient(self, n, k):
        """Вычисляет биномиальный коэффициент C(n, k)."""
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
