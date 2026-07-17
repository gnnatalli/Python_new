"""02 Фильтрация по символу
Создайте новый список, исключив все строки,
содержащие символ, который введет пользователь.

Данные:
words = ["apple", "cherry", "kiwi", "banana", "orange"]

Пример вывода:
Исключить символ: r
['apple', 'kiwi', 'banana']
"""

words = ["apple", "cherry", "kiwi", "banana", "orange"]
char = "r"  # input("Исключить символ: ")

res = [w for w in words if char not in w]
print(res)