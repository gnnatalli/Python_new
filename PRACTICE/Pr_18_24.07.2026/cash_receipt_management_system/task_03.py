"""Система управления кассовыми чеками

03 Добавление чеков

Доработайте Shift, чтобы
- чеки создавались только (!) через смену
    (композиция или агрегация?)

А именно:
- добавьте в Shift метод add_receipt(), который:
    - Создаёт объект Receipt с уникальным ID
        (ID чека уникален только в рамках текущей смены,
         каждая новая смена начинается с чека #1)
    - Сохраняет его внутри текущей смены
    - Если смена закрыта — выбрасывается ValueError:
        - ValueError("Cannot add receipts to a closed shift.")

Проверьте работу метода, создав несколько чеков внутри смены.
"""
from task_01 import Receipt

class Shift:
    _id_counter = 1

    def __init__(self):
        self.shift_id = Shift._id_counter
        Shift._id_counter += 1

        self.receipts = []
        self.closed = False

    def is_closed(self):
        return self.closed

    def close(self):
        self.closed = True

    def get_total(self):
        return sum(receipt.amount for receipt in self.receipts)

    def list_receipts(self):
        print(self.receipts)




    def add_receipt(self, amount):
        if self.is_closed():
            raise ValueError("Cannot add receipts to a closed shift.")
        receipt_id = len(self.receipts) + 1
        receipt = Receipt(receipt_id, amount)
        self.receipts.append(receipt)

if __name__ == "__main__":
    shift = Shift()
    shift.add_receipt(100)
    shift.add_receipt(200)
    shift.add_receipt(100)
    shift.list_receipts()
    print(shift.get_total())


# [Receipt 1: 100, Receipt 2: 200, Receipt 3: 100]
# 400