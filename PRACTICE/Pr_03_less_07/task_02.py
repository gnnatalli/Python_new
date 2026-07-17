""" 02. Сумма чисел

Напишите программу, которая
- принимает число от пользователя
- и выводит сумму с чисел от 1 до самого числа.

Пример вывода:
Введите число: 5
Сумма чисел от 1 до 5 = 15
"""

# x =  5
x = int(input('Введите число: '))
i = 1
s = 0

while i <= x:
    s += i
    i += 1

print ('Сумма чисел от 1 до',x,'=',s)

# 2-variant

number = int(input("Введите число: "))

check_number = number
sum_numbers = 0

while check_number > 0:
sum_numbers = sum_numbers + check_number
check_number -= 1
print ("Сумма чисел от:", number - number + 1, "до", number, "=", sum_numbers)