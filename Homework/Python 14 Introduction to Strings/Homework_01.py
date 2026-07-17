# 1. Проверка кодировки
# Напишите программу, которая принимает от пользователя один символ
# и выводит его код в таблице Unicode и его принадлежность к диапазону ASCII (True/False).
# Пример вывода:
# Введите символ: A
# Код Unicode: 65
# ASCII символ: True


symbol = input("Введите символ: ")

code = ord(symbol)

print("Код Unicode:", code)

if code < 128:
    print("ASCII символ: True")
else:
    print("ASCII символ: False")
