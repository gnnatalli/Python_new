""" Система управления кассовыми чеками

01. Класс Receipt
Создайте класс Receipt, представляющий чек.
Каждый чек должен иметь ID и сумму.
Метод __str__() должен возвращать строку формата:
Receipt <ID>: <amount>
"""
class Receipt:
    def __init__(self, recept_id, amount):
        self.recept_id = recept_id
        self.amount = amount

    def __str__(self):
        return f"Receipt {self.recept_id}: {self.amount}"
    def __repr__(self):
        return f"Receipt {self.recept_id}: {self.amount}"


if __name__ == "__main__":
    receipt = Receipt(1, 100)
    print(receipt)

    # Receipt 1: 100
