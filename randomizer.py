"""
 Класс для описания генератора последовательности случайных чисел.
"""
import random

class Randomizer:
    def __init__(self):
        pass

    def generate_random_number(self):
        """Генерирует случайное число в диапазоне от -100 до 100, исключая 0."""
        while True:
            random_number = random.randint(-100, 100)
            if random_number != 0:
                return random_number
