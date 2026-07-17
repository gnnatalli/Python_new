""" 03 Строки с длиной

Напишите программу, которая
- преобразует список строк в словарь, где
    ключи — сами строки,
    а значения — их длины.

Данные:
words = ["apple", "banana", "cherry", "date"]

Пример вывода:
{'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}
"""

words = ["apple", "banana", "cherry", "date"]
result = {word: len(word) for word in words}

print(result)
