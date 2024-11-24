"""
 Класс для описания игрового поля.
"""
import settings

class Board:

    def __init__(self):
        self.levels = settings.LEVELS
        print("Игровое поле инициализировано.")
        print(f"Количество уровней: {self.levels}")