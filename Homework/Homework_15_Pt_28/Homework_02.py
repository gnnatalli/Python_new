""" 02. Обновление цен товаров

Дан список товаров с ценами.
Программа должна
- применить скидку к каждому товару
- и добавить в список элемент с новой ценой.
- В конце вывести таблицу с новой ценой.

Данные:
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
Пример вывода:
Введите скидку (в процентах): 17

Товар          Старая цена    Новая цена
Laptop            1200.00$       996.00$
Mouse               25.00$        20.75$
Keyboard            75.00$        62.25$
Monitor            200.00$       166.00$

"""
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

discount = 17  # int(input("Введите скидку (в процентах): "))
print(int(input("Введите скидку (в процентах): ")))
# Добавляем новую цену в каждый товар
for product in products:
    old_price = product[1]
# Вычисляем новую цену
    new_price = old_price *(1 - discount / 100)
# Добавляем новую цену в список
    product.append(new_price)
# Заголовок таблицы
print(f"{'Товар':15} {'Старая цена':15} {'Новая цена':}")
# Вывод таблицы
for product in products:

    name = product[0]
    old_price = product[1]
    new_price = product[2]

    print(f"{name:15} {old_price:10.2f}$ {new_price:12.2f}$")




