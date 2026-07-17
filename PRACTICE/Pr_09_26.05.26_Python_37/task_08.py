""" 08 Рецепты по ингредиентам

Создайте словарь, в котором
- для каждого набора ингредиентов будут храниться все названия рецептов.

Учитывайте что ингредиенты могут быть перечислены в произвольном порядке и некоторые рецепты могут иметь одинаковые ингредиенты.
Выведите возможные рецепты для каждого набора продуктов.

В конце пользователь вводит список имеющихся у него ингредиентов через пробел,
и программа должна вывести названия всех доступных рецептов.

Если рецептов нет, нужно вывести сообщение "Нет рецептов".
Данные:
recipes = {
    ("flour", "egg", "milk"): "Pancakes",
    ("egg", "milk", "butter"): "Omelette",
    ("flour", "sugar", "butter"): "Cookies",
    ("flour", "egg", "butter", "sugar"): "Cake",
    ("milk", "flour", "egg"): "Waffles",
    ("butter", "milk", "egg"): "Scrambled Eggs",
    ("flour", "milk", "sugar", "butter"): "Sweet Bread"
}

Пример ввода:
milk egg butter flour

Пример вывода:
Ингредиенты                    | Рецепты
------------------------------------------------------------
flour, milk, egg               | Pancakes, Waffles
butter, milk, egg              | Omelette, Scrambled Eggs
flour, sugar, butter           | Cookies
flour, sugar, butter, egg      | Cake
flour, sugar, butter, milk     | Sweet Bread

Введите ингредиенты через пробел: milk egg butter flour
Доступные рецепты: Pancakes, Waffles, Omelette, Scrambled Eggs
"""

# recipes = {
#     ("flour", "egg", "milk"): "Pancakes",
#     ("egg", "milk", "butter"): "Omelette",
#     ("flour", "sugar", "butter"): "Cookies",
#     ("flour", "egg", "butter", "sugar"): "Cake",
#     ("milk", "flour", "egg"): "Waffles",
#     ("butter", "milk", "egg"): "Scrambled Eggs",
#     ("flour", "milk", "sugar", "butter"): "Sweet Bread"
# }
#
# # user_input = input("Введите ингредиенты через пробел:" )
# user_input = "milk egg butter flour"
# user_set = set(user_input.split())
#
# found = []
#
# for ingredients, name in recipes.items():
#     if set(ingredients) <= user_set:
#         found.append(name)
#
# if len(found) > 0:
#     print("Доступные рецепты:", ", ".join(found))
# else:
#     print("Нет рецептов")


recipes = {
("flour", "egg", "milk"): "Pancakes",
("egg", "milk", "butter"): "Omelette",
("flour", "sugar", "butter"): "Cookies",
("flour", "egg", "butter", "sugar"): "Cake",
("milk", "flour", "egg"): "Waffles",
("butter", "milk", "egg"): "Scrambled Eggs",
("flour", "milk", "sugar", "butter"): "Sweet Bread"
}

print("""
Ингредиенты | Рецепты
------------------------------------------------------------""")
for k, v in recipes.items():
print(f"{", ".join(k):30} | {v}")

print()
ingredients = input("Введите ингредиенты через пробел: ").split()

available_recipes = []
for k, v in recipes.items():
if set(k) <= set(ingredients):
available_recipes.append(v)

print("Доступные рецепты:", ", ".join(available_recipes))