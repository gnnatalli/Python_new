# Удаление всех повторяющихся символов
#
# Напишите программу, которая принимает строку и удаляет из неё все повторяющиеся символы,
# сохраняя только первые их вхождения.
#
# Пример вывода:
#
# Введите строку: Python programming
#
# Результат: Python prgami


text = input("Введите строку: ")

result = ""

for char in text:
    if char not in result:
        result = result + char

print("Результат: ", result)