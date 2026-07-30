"""Система управления кассовыми чеками

06. Обновление Shift для работы с подклассами чеков

Измените следующие методы в класс Shift:

- Метод add_receipt(amount):
    - должен создавать объекты класса SaleReceipt (вместо Receipt)

- Метод add_return(original_id, return_amount)
    - должен создавать объекты класса ReturnReceipt  (вместо Receipt)

Доработайте уже существующие методы:
- list_receipts(receipt_type=None), который возвращает список всех чеков:
    - Если receipt_type=None — список всех чеков
    - Если receipt_type="sale" — только чеки продаж (SaleReceipt)
    - Если receipt_type="return" — только возвраты (ReturnReceipt)

- get_total(receipt_type=None) который возвращает сумму:
    - Всех чеков, если receipt_type=None
    - Только продаж, если receipt_type="sale"
    - Только возвратов, если receipt_type="return"
"""

from task_05 import Receipt, SaleReceipt, ReturnReceipt

class Shift:
    _id_counter = 1

    def __init__(self)
        self.id = Shift._id_counter
        Shift._id_counter += 1

        self.receipts = []
        self.closed = False

    def is_closed(self):
        return self.closed

    def close(self):
        self.closed = True

    def add_receipt(self, amount):

        if self.is.closed():
            raise ValueError(
                "Can not add receipt to a closed Shift"
            )

        receipt_id = len(self.receipts) + 1

        receipt = SaleReceipt(receipt_id, amount)

        self.receipts.append(receipt)

        return receipt

    def add_return(self, source_shift, original_id, return_amount):
#         Ищем исходной текст
        original_receipt = next(receipt for receipt in source_shift.receipts if receipt.receipt_id == original_id), None

        if original_receipt is None:
            raise ValueError(
                "Original Receipt not found."
            )




