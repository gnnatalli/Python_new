""" 03 Самое длинное слово
Дано предложение.
Найдите самое длинное слово
и выведите это слово с его длиной.

Данные:
sentence = "Programming in Python is both fun and educational"

Пример вывода:
Самое длинное слово: Programming
Длина слова: 11
"""

sentence = "Programming in Python is both fun and educational"
max_word = max(sentence.split(),key=len)
print(f'Самое длинное слово: {max_word}\nДлина слова: {len(max_word)}')
