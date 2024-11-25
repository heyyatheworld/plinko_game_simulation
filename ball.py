"""
Класс для описания шарика.
"""
from settings import BET_MODE


#from settings import *

class Ball:
    def __init__(self, start_position, rng):
        """
        Инициализирует новый экземпляр класса Ball.

        Параметры:
            start_position (tuple): Начальная позиция шарика (уровень, индекс).
            rng (Randomizer): Экземпляр генератора случайных чисел.
        """
        self.position = start_position  # Позиция шарика (уровень, индекс)
        self.rng = rng  # Экземпляр генератора случайных чисел
        if BET_MODE == "Manual":
            print(f"{'Старт: ':<15} {self.position[0]:3}, индекс {self.position[1]:3}")

    def move(self):
        """Перемещает шарик вниз по треугольнику Паскаля."""
        level, index = self.position
        random_value = self.rng.generate_random_number()

        if random_value < 0:
            # Двигаемся влево
            new_index = max(index, 0)  # Убедимся, что индекс не выходит за пределы
            if BET_MODE == "Manual":
                print(f"{'<<< на уровень':<15} {level + 1:3}, индекс {new_index:3} ", end='')
            self.position = (level + 1, new_index)
            #self.display_current_level(level)
        elif random_value > 0:
            # Двигаемся вправо
            new_index = index + 1
            if BET_MODE == "Manual":
                print(f"{'>>> на уровень':<15} {level + 1:3}, индекс {new_index:3} ", end='')
            self.position = (level + 1, new_index)
            #self.display_current_level(level)

    def get_position(self):
        """Возвращает текущую позицию шарика."""
        return self.position
