from settings import *
import math


class Benefits:
    def __init__(self):
        self.rows = LEVELS + 1  # Увеличиваем количество рядов на 1
        self.rtpmin = RTPMIN
        self.rtpmax = RTPMAX


    def binomial_coefficient(self, n, k):
        """Вычисляет биномиальный коэффициент C(n, k)."""
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    def last_row_cells_and_probabilities(self):
        """Возвращает значения ячеек последнего ряда и вероятности попадания в них."""
        last_row_index = self.rows - 1
        last_row_values = [self.binomial_coefficient(last_row_index, k) for k in range(last_row_index + 1)]

        total_paths_to_last_row = sum(last_row_values)
        probabilities = [value / total_paths_to_last_row for value in
                         last_row_values] if total_paths_to_last_row > 0 else [0] * len(last_row_values)
        return last_row_values, probabilities

    def calculate_min_multipliers(self):
        last_row_values, probabilities = self.last_row_cells_and_probabilities()
        min_multipliers = [
            ((self.rtpmin/100) / prob) if prob > 0 else float('inf') for prob in probabilities
        ]
        return min_multipliers
