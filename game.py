"""
 Основной класс игры.
"""
from settings import *
from randomizer import Randomizer
from ball import Ball
from benefits import Benefits
from account import Account

class Game:

    def __init__(self):
        #self.rtp = RTP
        self.bet = STANDARD_BET
        self.level = LEVEL
        self.games_in_stage = GAMES_IN_STAGE
        self.mult = MLT_LVL[self.level]
        self.bet_mode = BET_MODE
        self.rtp = 0
        self.total_bet = 0
        self.total_win = 0
        self.game_number = 0

        self.benefits = Benefits()
        self.account = Account()

    def start_game(self):
        print("\nСимулятор Plinko:")
        print("-----------------------------")
        print(f"Количество уровней: {self.level}")
        print(f"Режим игры        : {self.bet_mode}")
        print("-----------------------------")

    def play(self):
        """Основной игровой процесс."""
        self.start_game()  # Запуск игры

        while True:
            user_input = input(
                "'Enter' или 'exit' ...")

            if user_input == '':
                self.run_stage()

            elif user_input.lower() == 'exit':
                break
        print("Игра окончена!")

    def run_stage(self):
        """Логика для выполнения этапа игры."""
        rng_instance = Randomizer()  # Создаем экземпляр генератора случайных чисел
        print()
        if BET_MODE == "Manual": self.games_in_stage = 1
        if BET_MODE == "Auto": self.games_in_stage = 1000

        for i in range(self.games_in_stage):
            if BET_MODE == "Manual": print(f"# {self.game_number:5}")
            self.game_number += 1
            bet = self.bet
            self.total_bet += bet
            self.account.withdraw(self.bet)

            start_pos = (0, 0)
            ball = Ball(start_pos, rng_instance)

            for _ in range(self.level):
                ball.move()
                if BET_MODE == "Manual": print(f" Текущая позиция: {ball.get_position()}")

            if BET_MODE == "Manual":
                print(f"Множители текущего уровня:")
                for i in range(self.level + 1):
                    print(f"|  {self.mult[i]}  |", end='')
                print()

            win = bet*self.mult[ball.get_position()[1]]
            self.total_win += win
            self.account.deposit(win)

            self.rtp = self.total_win / self.total_bet * 100

        print(f"Сыграно игр  : {self.game_number}")
        print(f"Баланс игрока: {self.account.get_balance()}")
        print(f"Текущий RTP  : {self.rtp:.2f}%")
