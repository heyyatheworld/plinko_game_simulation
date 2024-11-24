"""
 Основной класс игры.
"""
import settings
from rng import Rng

class Game:

    def __init__(self):
        self.levels = settings.LEVELS
        self.rtpmin = settings.RTPMIN
        self.rtpmax = settings.RTPMAX

        self.bet_mode = "Manual" # Manual Auto
        self.risk_level = "Low" # Low Normal High

        self.rng = Rng()


    def start_game(self):
        print("\nНастройки игры:")
        print("-----------------------------")
        print(f"Количество уровней: {self.levels}")
        print(f"Режим игры        : {self.bet_mode}")
        print(f"Уровень риска     : {self.risk_level}")
        print("-----------------------------\n")

    def end_game(self):
        print("Игра окончена!")

    def play(self):
        """Основной игровой процесс."""
        self.start_game()  # Запуск игры

        while True:
            user_input = input(
                "Введите 'exit' для выхода или нажмите 'Enter' для запуска уровня: ")  # Ожидаем ввода от пользователя

            if user_input == '':  # Проверяем, нажата ли клавиша 'Enter'
                self.run_stage(self.levels)  # Запуск уровня

            elif user_input.lower() == 'exit':  # Проверяем ввод на 'exit'
                print("Выход из игры...")
                break  # Выход из цикла

        self.end_game()  # Завершение игры

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
        print(f"Последовательность случайных чисел: {self.rng.generate_random_sequence()}")
        print("Этап игры завершён!")
