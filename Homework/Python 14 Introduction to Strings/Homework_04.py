# Инвертирование строки без цифр
#
# Напишите программу, которая принимает строку и выводит её в обратном порядке,
# пропуская все цифры.
#
# Пример вывода:
#
# Введите строку: n52uFs6Inoh67ty8P
# Результат: PythonIsFun

text = input("Введите строку: ")

filtered = ""
i = 0

while i < len(text):
    if not text[i].isdigit():
        filtered += text[i]
    i += 1
result = filtered[::-1]
print("Результат: ", result)