"""Система управления кассовыми чеками

02. Класс Shift

Создайте класс Shift, представляющий кассовую смену.
У каждой смены
- свой уникальный ID: _id_counter (нумерация с 1)

Кроме того, у смены есть:
- список чеков
- статус (открыта или закрыта)

Реализуйте методы:
- is_closed() — возвращает закрыта ли смена
- close() — закрывает смену
- get_total() — возвращает сумму всех чеков
- list_receipts() — выводит список чеков через print()
"""

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
        return sum(receipt.amount for receipt in self.receipts())

    def list_receipts(self):
        print(self.receipts())


