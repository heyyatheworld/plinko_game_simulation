"""
 Основной класс игры.
"""
from settings import *
from rng import Rng
from ball import Ball
from benefits import Benefits
from account import Account

class Game:

    def __init__(self):
        self.levels = LEVELS
        self.rtpmin = RTP
        self.bet = BET

        self.bet_mode = "Manual" # Manual Auto
        #self.bet_mode = "Auto"  # Manual Auto
        self.risk_level = "Low" # Low Normal High

        self.games_in_stage = 100

        self.benefits = Benefits()
        self.account = Account()

        last_row_values, probabilities = self.benefits.last_row_cells_and_probabilities()

        print(f"{'Значения: ':<13} {str(last_row_values):6} {str(sum(last_row_values)):5}")
        print(f"{'Вероятности:':<13} {str(probabilities):6} {str(sum(probabilities)):5}")

        min_multipliers = self.benefits.calculate_min_multipliers()
        print("Множители для RTP 75%:", min_multipliers)


    def start_game(self):
        print("\nНастройки игры:")
        print("-----------------------------")
        print(f"Количество уровней: {self.levels}")
        print(f"Режим игры        : {self.bet_mode}")
        print(f"Уровень риска     : {self.risk_level}")
        print("-----------------------------")

        self.mult = MLLVL[self.levels]
        print(f"*: |", end='')
        for i in range(self.levels+1):
            print(f" {self.mult[i]} |", end='')
        print()

    def end_game(self):
        print("Игра окончена!")

    def play(self):
        """Основной игровой процесс."""
        self.start_game()  # Запуск игры

        while True:
            print(f"Баланс: {self.account}")
            user_input = input(
                "Введите 'exit' для выхода или нажмите 'Enter' для продолжения: \n")  # Ожидаем ввода от пользователя

            if user_input == '':
                print("\033[5F", end='')
                print("\n" * 100)  # Печатает 100 пустых строк
                self.run_stage(self.levels)

            elif user_input.lower() == 'exit':
                print("Выход из игры...")
                break  # Выход из цикла

        self.end_game()  # Завершение игры

    def run_stage(self, level):
        """Логика для выполнения этапа игры."""
        rng_instance = Rng()  # Создаем экземпляр генератора случайных чисел

        if self.bet_mode == "Manual":
            #print(f"Последовательность случайных чисел: {rng_instance.generate_random_sequence()}")
            bet = self.bet
            self.account.withdraw(self.bet)
            start_pos = (0, 0)  # Начальная позиция на уровне 0, индекс 0
            ball = Ball(start_pos, rng_instance)

            # Перемещение шарика несколько раз
            for _ in range(self.levels):
                ball.move()
                print(f" Текущая позиция: {ball.get_position()}")
            position = ball.get_position()[1]
            print(f"  Мультик: {self.mult[position]}")
            bet = bet*self.mult[position]
            self.account.deposit(bet)
            print("\nЭтап игры завершён!")

        if self.bet_mode == "Auto":
            for i in range(1,self.games_in_stage+1):
                print(f"Испытание {i}: {rng_instance.generate_random_sequence()}")


