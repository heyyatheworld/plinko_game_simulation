from ball import Ball
from account import Account
from benefits import Benefits
from randomizer import Randomizer

from settings import *

class Game:

    def __init__(self):
        self.bet = STANDARD_BET
        #self.level = LEVELS
        self.games_in_stage = GAMES_IN_STAGE
        self.mult = () #X_LVL[self.level]
        self.bet_mode = BET_MODE
        self.rtp = 0
        self.total_bet = 0
        self.total_win = 0
        self.game_number = 0
        self.benefits = Benefits()
        self.account = Account()

    def run_stage(self):
        print("\nСимулятор Plinko:")
        rng_instance = Randomizer()
        for lvl in range(5, LEVELS + 1):

            self.rtp = 0
            self.total_win = 0
            self.total_bet = 0

            for i in range(self.games_in_stage):
                    bet = self.bet
                    self.total_bet += bet
                    self.account.withdraw(self.bet)

                    start_pos = (0, 0)
                    ball = Ball(start_pos, rng_instance)
                    for _ in range(lvl):
                        ball.move()

                    win = bet * X_LVL[lvl][ball.get_position()[1]]
                    self.account.deposit(win)
                    self.total_win += win

            self.rtp = self.total_win / self.total_bet * 100
            print(f"Уровень: {lvl:2d}  ", end='')
            print(' '*4*(LEVELS-lvl), end='')
            for j in range(lvl + 1):
                if X_LVL[lvl][j] < 10:
                    print(f"  {X_LVL[lvl][j]:3.2f}  ", end='')
                else:
                    print(f"  {X_LVL[lvl][j]:3.1f}  ", end='')
            print(' ' * 4 * (LEVELS - lvl), end='')
            print(f" RTP: {self.rtp:3.2f}%")
