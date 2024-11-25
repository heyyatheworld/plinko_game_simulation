"""
 Основной класс приложения.
"""
import random

from ball import Ball
from account import Account
from settings import *

class Game:

    def __init__(self):
        self.account = Account()

    def run_stage(self):
        """Основной цикл приложения. Проходит серия симуляций."""
        print("\nСимулятор Plinko:\n")
        number_of_tests = 0

        #В цикле проходим по уровням игры от 5 до 14."""
        for current_level in range(5, LEVELS + 1):
            return_to_player = 0
            total_win = 0
            total_bet = 0
            bet = STANDARD_BET

            #Для каждого уровня проходим определённое кол-во испытаний.
            for i in range(GAMES_IN_STAGE):

                #Подсчитываем все потраченные на уровне средства.
                self.account.withdraw(bet)
                total_bet += bet

                start_pos = (0, 0)
                #Проходим один раз всё игровое поле.
                ball = Ball(start_pos)
                for _ in range(current_level):
                    ball.move()

                #Определяем результат текущего раунда.
                win = bet * MULT_LEVELS[current_level][ball.get_position()[1]]

                #Подсчитываем все полученные на уровне средства.
                self.account.deposit(win)
                total_win += win

                #Подсчитываем количество испытаний.
                number_of_tests += 1

            #Подсчитываем RTP как отношение всех полученных к всем потраченным на уровне средствам.
            return_to_player = total_win / total_bet * 100

            #Попытка форматированного вывода результатов в консоль.
            print(f"Уровень: {current_level:2d}  ", end='')

            print(' ' * 4 * (LEVELS - current_level), end='')
            for j in range(current_level + 1):
                if MULT_LEVELS[current_level][j] < 10:
                    print(f"  {MULT_LEVELS[current_level][j]:3.2f}  ", end='')
                else:
                    print(f"  {MULT_LEVELS[current_level][j]:3.1f}  ", end='')
            print(' ' * 4 * (LEVELS - current_level), end='')

            print(f" RTP: {return_to_player:3.2f}%")

        print(f"\nВсего проведено испытаний: {number_of_tests:6d}.")
