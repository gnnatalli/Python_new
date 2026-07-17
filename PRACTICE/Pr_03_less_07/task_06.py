""" 06. Последовательности Фибоначчи
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

Напишите программу, в которой
- Пользователь вводит число n,
- после чего программа выводит первые n чисел последовательности Фибоначчи.

Пример вывода:
Введите количество чисел: 7
0 1 1 2 3 5 8
"""

n = int(input("Введите количество чисел: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")

    next_number = a + b
    a = b
    b = next_number

    count = count + 1

# 2 - variant
num = int(input("Введите количество чисел: "))
a, b = 0, 1
i = 0

while i < num:
    print(a, end = " ")
    a, b = b, a + b
    i += 1