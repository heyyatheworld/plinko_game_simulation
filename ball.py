"""
Класс для описания шарика.
"""
from settings import *

class Ball:
    def __init__(self, start_position, rng):
        """
        Инициализирует новый экземпляр класса Ball.

        Параметры:
            start_position (tuple): Начальная позиция шарика (уровень, индекс).
            rng (Rng): Экземпляр генератора случайных чисел.
        """
        self.position = start_position  # Позиция шарика (уровень, индекс)
        self.rng = rng  # Экземпляр генератора случайных чисел
        print(f"{'Старт: ':<15} {self.position[0]:3}, индекс {self.position[1]:3}")

    def move(self):
        """Перемещает шарик вниз по треугольнику Паскаля."""
        level, index = self.position
        random_value = self.rng.generate_random_number()

        if random_value < 0:
            # Двигаемся влево
            new_index = max(index, 0)  # Убедимся, что индекс не выходит за пределы
            print(f"{'<<< на уровень':<15} {level + 1:3}, индекс {new_index:3} ", end='')
            self.position = (level + 1, new_index)
            #self.display_current_level(level)
        elif random_value > 0:
            # Двигаемся вправо
            new_index = index + 1
            print(f"{'>>> на уровень':<15} {level + 1:3}, индекс {new_index:3} ", end='')
            self.position = (level + 1, new_index)
            #self.display_current_level(level)
        else:
            # Если random_value == 0, шарик остается на месте
            print(f"Шарик остается на уровне {level}, индекс {index}", end='')

    def get_position(self):
        """Возвращает текущую позицию шарика."""
        return self.position

    def display_current_level(self, levels):
        """Выводит текущий уровень треугольника Паскаля."""
        level = self.position[0]

        if level < LEVELS-2:
            row_str = []
            for index in range(level + 1):
                if index == self.position[1]:
                    row_str.append('X')  # Позиция шарика
                else:
                    row_str.append('_')  # Пустая ячейка

            print(" ".join(row_str).center(len(" ".join(map(str, levels[level])))))
        else:
            print("Шарик вышел за пределы треугольника.")

def generate_pascals_triangle(levels):
    """Генерирует треугольник Паскаля."""
    triangle = []

    for i in range(levels):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle