""" 04 Максимальное число

Напишите программу, которая
- выводит наибольшее число в списке (не используя встроенную функцию max()!!!),
- а также его индекс в списке.

numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
Пример вывода:
Список чисел: [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
Наибольшее число: 25
Индекс числа: 5
"""

numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]

#max_element = numbers[0]
max_index = 0

for i in range(1, len(numbers)):
    if numbers[max_index] < numbers[i]:
        #max_element = numbers[i]
        max_index = i


print("Список чисел:", numbers)
print("Наибольшее число:", numbers[max_index])
print("Индекс числа:", max_index)