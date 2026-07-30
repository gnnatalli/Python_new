""" 02 История операций

Доработайте класс BankAccount:
- каждая операция пополнения и снятия должна сохраняться в историю history
- история операций должна
    - вызываться через атрибут history (только для чтения!)
    - и выводить на печать список операций в формате:

Operation history:
    Deposit: 150
    Withdraw: 100

⚠️ Важно:
Если история содержит изменяемый тип данных (список), то
злоумышленник сможет легко получить доступ и этому списку и изменить его!
При решении необходимо это учесть.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self._history = []

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
        else:
            self._balance += amount
            self._history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
        else:
            self._balance -= amount
            self._history.append(f"Withdraw: {amount}")

    def show_balance(self):
        print(f"Current balance: {self._balance}.")

    @property
    def history(self):
        return self._history.copy()



if __name__ == "__main__":
    account = BankAccount("Alice", 50)

    account.deposit(150)
    account.withdraw(100)
    account.show_balance()

    print("Operation history:")
    for operation in account.history:
        print("\t", operation)

    account.history.append('injection')
    if account.history != ["Deposit: 150", "Withdraw: 100"]:
        print("ВНИМАНИЕ! \nАККАУНТ ВЗЛОМАН! \nИстория операций изменена хакерами!!!")


# Current balance: 100
# Operation history:
# 	 Deposit: 150
# 	 Withdraw: 100


"""
Если задаче решена верно, то этого сообщения вы не увидите:

ВНИМАНИЕ! 
АККАУНТ ВЗЛОМАН! 
История операций изменена хакерами!!!
"""
