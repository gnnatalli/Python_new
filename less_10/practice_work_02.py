""" 02 Список имён

Напишите программу, которая
- обрабатывает список строк, состоящий из имен.

Нужно вывести только те имена, длина которых больше средней длины имен в списке.

Пример вывода:
Список имён: ['John', 'Bob', 'Alice', 'Anna', 'Mark']
Средняя длина имён: 4.0
Имена длиннее средней длины: ['Alice']
"""

names = ['John', 'Bob', 'Alice', 'Anna', 'Mark']

total_length = 0
for name in names:
    total_length = total_length + len(name)

average_length = total_length / len(names)

longer_names = []
for name in names:
    if len(name) > average_length:
        longer_names = longer_names + [name]

print("Список имён:", names)
print("Средняя длина имён:", average_length)
print("Имена длиннее средней длины:", longer_names)