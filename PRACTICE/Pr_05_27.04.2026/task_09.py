""" 09 Звёздочки вместо чисел

Напишите программу, которая заменяет все цифры в строке на звёздочки *.

Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-***
"""

text = "My number is 123-456-789"
result = ""

for char in text:
    if char.isdigit():
        result += "*"
    else:
        result += char

print("Строка: ", text)
print("Результат: ", result)