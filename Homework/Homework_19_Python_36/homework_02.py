""" 02 Счётчик букв в словах

Напишите программу, которая
- подсчитывает количество каждой буквы в заданных словах
- и создаёт словарь, где
        ключи — это слова,
        а значения — это ещё один словарь, где
                ключ - это буква,
                а значение - число повторений этой буквы в слове.
Данные:
words = ["anna", "bennet", "john"]

Пример вывода:
{'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}

"""

words = ["anna", "bennet", "john"]

result = {}

for word in words:
    letter_count = {}

    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    result[word] = letter_count

print(result)