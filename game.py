"""
 Основной класс игры.
"""
import settings

class Game:

    def __init__(self):
        self.levels = settings.LEVELS
        self.rtpmin = settings.RTPMIN
        self.rtpmax = settings.RTPMAX
        print("Игра началась!")
        print(f"Количество уровней: {self.levels}")

    def start_game(self):
        print("Игра запущена!")

    def end_game(self):
        print("Игра окончена!")

    def play(self):
        """Основной игровой процесс."""
        self.start_game()

        self.run_stage(self.levels)  # Запускаем уровень

        self.end_game()

    def run_stage(self, level):
        """Логика для выполнения этапа игры.
        while True:

            if True:
                pass

            elif False:
                pass

            else:
                pass
        """
        print("Этап игры завершён!")
