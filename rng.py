"""
 Класс для описания генератора последовательности случайных чисел.
"""
import random
import settings

class Rng:
    def __init__(self):
        self.levels = settings.LEVELS
        #print(f"Количество уровней: {self.levels}")

    def generate_random_number(self):
        self.min_value = -100
        self.max_value = 100
        random_number = random.randint(self.min_value, self.max_value)
        #print(f"Сгенерированное случайное число: {random_number}")
        return random_number

    def generate_random_sequence(self):
        sequence = [self.generate_random_number() for _ in range(self.levels)]
        return sequence

    def update_sequence_periodically(self):
            self.generate_random_sequence()

    def set_levels(self, new_levels):
        self.levels = new_levels
        print(f"Количество уровней обновлено: {self.levels}")
