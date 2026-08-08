""" 02. Увеличение цен

Продолжите предыдущую задачу. Теперь программа должна:
- увеличить цену всех товаров на 20%
- вывести количество обновлённых записей
- затем вывести список всех товаров с новыми ценами

Пример вывода:
Prices updated for 3 products.

Updated products:
- Pen — $1.80
- Notebook — $4.79
- Backpack — $30.00"""


from pymongo import MongoClient
from local_settings import MONGODB_URL_WRITE

with MongoClient(MONGODB_URL_WRITE) as client:
    db = client["ich_edit"]

    collection = db[
        "products_060326_ptm_Nataliia_Honchar"
    ]

    # Увеличиваем цену всех товаров на 20%
    result = collection.update_many(
        {},
        {
            "$mul": {
                "price": 1.2
            }
        }
    )

    print(
        f"Prices updated for {result.modified_count} products."
    )

    print("\nUpdated products:")

    for product in collection.find({}, {"_id": 0}):
        print(
            f"- {product['name']} - ${product['price']:.2f}"
        )
# Prices updated for 3 products.
#
# Updated products:
# - Laptop — $1440.00
# - Mouse — $30.00
# - Keyboard — $84.00