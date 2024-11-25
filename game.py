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
        self.rtp = RTP
        self.bet = BET
        self.levels = LEVELS
        self.games_in_stage = GIS
        self.mult = MLLVL[self.levels]
        self.bet_mode = "Manual" # Manual Auto
        self.risk_level = "Low" # Low Normal High

        self.benefits = Benefits()
        self.account = Account()

    def start_game(self):
        print("\nНастройки игры:")
        print("-----------------------------")
        print(f"Количество уровней: {self.levels}")
        print(f"Режим игры        : {self.bet_mode}")
        print(f"Уровень риска     : {self.risk_level}")
        print("-----------------------------")

    def play(self):
        """Основной игровой процесс."""
        self.start_game()  # Запуск игры

        while True:
            print(f"Баланс: {self.account}")
            user_input = input(
                "'Enter' или 'exit' ...\n")

            if user_input == '':
                self.run_stage()

            elif user_input.lower() == 'exit':
                break
        print("Игра окончена!")

    def run_stage(self):
        """Логика для выполнения этапа игры."""
        rng_instance = Rng()  # Создаем экземпляр генератора случайных чисел

        if self.bet_mode == "Manual":

            bet = self.bet
            self.account.withdraw(self.bet)

            start_pos = (0, 0)
            ball = Ball(start_pos, rng_instance)

            for _ in range(self.levels):
                ball.move()
                print(f" Текущая позиция: {ball.get_position()}")

            for i in range(self.levels + 1):
                print(f" {self.mult[i]} |", end='')
            print()

            bet = bet*self.mult[ball.get_position()[1]]
            self.account.deposit(bet)

        if self.bet_mode == "Auto":
            for i in range(self.games_in_stage):
                pass
