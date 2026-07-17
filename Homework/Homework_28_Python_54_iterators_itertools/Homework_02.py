""" 02 Объединение списков продуктов

Напишите функцию, которая
- принимает несколько (много) списков с названиями продуктов
- и возвращает генератор, содержащий все продукты в нижнем регистре.

Выведите содержимое генератора.

Данные:
fruits = ["Apple", "Bansana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt
"""

from itertools import chain

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

# *args - принимает любое количество списков
def gen(*args):
    # chain(*args) - склеивает все списки в один поток. (item.lower() for item in ...) - это генератор
    return (item.lower() for item in chain(*args))

result = gen(fruits, vegetables, dairy)
# for item in result - вывод результата
for item in result:
    print(item)

