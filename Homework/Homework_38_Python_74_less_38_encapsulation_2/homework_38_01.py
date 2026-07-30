""" 01 Банковский счёт

Экземпляр класса BankAccount должен содержать:
- имя владельца
- и текущий баланс.

Реализуйте методы:
- пополнение счёта deposit()
    - при попытке внести отрицательную сумму:
        - печатает "Error: Amount must be positive."
    - иначе:
        - увеличивает баланс на сумму пополнения

- снятие средств withdraw():
    - при попытке внести отрицательную сумму:
        - печатает "Error: Amount must be positive."
    - при попытке снять больше, чем есть на счёте:
        - печатает "Error: Not enough funds."
    - иначе:
        - уменьшает баланс на сумму снятия

- отображение баланса show_balance():
    - печатает: "Current balance: <сумма баланса>"

Подумайте:
- какие атрибуты и методы следует скрыть от внешнего доступа,
- а какие оставить открытыми.
"""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
        else:
            self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
        elif amount > self._balance:
            print("Error: Not enough funds.")
        else:
            self._balance -= amount

    def show_balance(self):
        print(f"Current balance: {self._balance}")


if __name__ == "__main__":
    account = BankAccount("Alice", 150)

    account.show_balance()
    account.deposit(-50)
    account.show_balance()
    account.withdraw(200)
    account.show_balance()
    account.deposit(100)
    account.show_balance()
    account.withdraw(50)
    account.show_balance()

# Current balance: 150
# Error: Amount must be positive.
# Current balance: 150
# Error: Not enough funds.
# Current balance: 150
# Current balance: 250
# Current balance: 200