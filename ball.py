"""
 Класс для описания шарика.
"""
import settings

class Ball:

    def __init__(self):
        self.levels = settings.LEVELS
        print("Шарик запущен.")
        print(f"Количество уровней: {self.levels}")