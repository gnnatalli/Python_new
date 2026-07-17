""" 01 Повторения букв

Реализуйте функцию, которая
- принимает текст
- и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.

Данные:
text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
"""

from collections import Counter

def char_count(text):
#     # Переводим все буквы в нижний регистр, чтобы Р и р читались одной буквой
    text = text.lower()
#     # Берем только буквы, игнорируя пробелы и знаки препинания
    letters = [char for char in text if char.isalpha()]
#     # Counter автоматически считает количество повторений
    return dict(Counter(letters))

text = "Programming is fun!"
sample = {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}


print(char_count(text))
print(char_count(text) == sample)
