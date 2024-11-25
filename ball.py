"""
ball.py
"""
import random

def generate_random_number():
    """Генерирует случайное число в диапазоне от -100 до 100, исключая 0."""
    while True:
        random_number = random.randint(-100, 100)
        if random_number != 0:
            return random_number

class Ball:
    """
     Класс для управления игровым элементом.
    """
    def __init__(self, start_position):
        self.position = start_position  # Позиция шарика (уровень, индекс)

    def move(self):
        """Перемещает шарик вниз на один уровень."""
        level, index = self.position
        random_value = generate_random_number()

        if random_value < 0:
            # Двигаемся влево
            new_index = max(index, 0)  # Убедимся, что индекс не выходит за пределы
            self.position = (level + 1, new_index)
        elif random_value > 0:
            # Двигаемся вправо
            new_index = index + 1
            self.position = (level + 1, new_index)

    def get_position(self):
        """Возвращает текущую позицию шарика."""
        return self.position
