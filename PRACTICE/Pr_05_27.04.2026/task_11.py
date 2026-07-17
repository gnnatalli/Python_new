""" 11 Количество символов

Напишите программу, которая подсчитывает количество:
- букв;
- цифр;
- пробелов;
- остальных символов.

Пример вывода:
Строка: Python 3.12 is awesome!
Буквы: 15
Цифры: 3
Пробелы: 3
Остальные символы: 2
"""

text = "Python 3.12 is awesome!"

letters = 0
digits = 0
spaces = 0
others = 0

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1

print("Строка: ", text)
print("Буквы: ", letters)
print("Цифры: ", digits)
print("Пробелы ", spaces)
print("Остальные символы: ", others)