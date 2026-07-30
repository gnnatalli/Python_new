"""Система управления кассовыми чеками

05. Классы SaleReceipt и ReturnReceipt

Доработайте систему чеков:
- создайте 2 дочерних класса
    - SaleReceipt(Receipt) и
    - ReturnReceipt(Receipt)


При создании SaleReceipt
- проверяйте, что сумма положительная

При создании ReturnReceipt
- проверяйте, что сумма отрицательная

В обоих случаях, если сумма нарушает правило, выбрасывается ValueError:
- ValueError("SaleReceipt amount must be positive.")
- ValueError("ReturnReceipt amount must be negative.")

Добавьте метод __str__(), возвращающий строку в формате:
<ReceiptClass> <ID>: +<amount>
<ReceiptClass> <ID>: -<amount>
"""

class Receipt:

    def __init__(self, receipt_id, amount):
        self.receipt_id = receipt_id
        self.amount = amount

class SaleReceipt(Receipt):

    def __init__(self, receipt_id, amount):
        if amount <= 0:
            raise ValueError("SaleReceipt amount must be positive.")

        super().__init__(receipt_id, amount)


    def __str__(self):
        return f"SaleReceipt {self.receipt_id}: +{self.amount}"

    def __repr__(self):
        return str(self)

class ReturnReceipt(Receipt):
    def __init__(self, receipt_id, amount):
        if amount >= 0:
            raise ValueError("ReturnReceipt amount must be negative.")

        super().__init__(receipt_id, amount)

    def __str__(self):
        return f"ReturnReceipt {self.receipt_id}: {self.amount}"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    receipts = []

    receipts.append(SaleReceipt(1, 1500))
    receipts.append(SaleReceipt(2, 700))
    receipts.append(ReturnReceipt(3, -300))

    print(receipts)

    print("Общий итог:", sum(r.amount for r in receipts))

# [SaleReceipt 1: +1500, SaleReceipt 2: +700, ReturnReceipt 3: -300]
# Общий итог: 1900
