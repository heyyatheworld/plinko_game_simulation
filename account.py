"""
account.py
"""
from settings import INITIAL_BALANCE

class Account:
    """
     Класс для управления игровым счётом.
    """
    def __init__(self):
        self.balance = INITIAL_BALANCE

    def deposit(self, amount):
        """Добавляет средства на счет."""
        if amount > 0:
            self.balance += amount
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        """Снимает средства со счета."""
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print(amount, self.balance)
            print("Недостаточно средств или сумма некорректна.")

    def get_balance(self):
        """Возвращает текущий баланс."""
        return self.balance
