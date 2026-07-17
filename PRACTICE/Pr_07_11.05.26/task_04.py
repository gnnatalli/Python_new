""" 04 Перемещение в конец

Напишите программу, которая модифицирует текущий список,
    перемещая все элементы меньше 5, в конец списка,
    но сохраняя при этом порядок остальных элементов.

ВАЖНО: НЕ создаём новый список, а модифицируем уже существующий!

Данные:
numbers = [4, 3, 7, 1, 2, 6, 3, 4, 8, 2]

Пример вывода:
Перемещённые элементы: [7, 6, 8, 4, 3, 1, 2, 3, 4, 2]
"""
FLAG = 5
numbers = [4, 3, 7, 1, 2, 6, 3, 4, 8, 2]
# numbers = [4, 3, 7]
l = len(numbers)
idx_for_del = []

print(id(numbers))
for i in range(l):
    if numbers[i] < FLAG:
        numbers.append(numbers[i])
        idx_for_del.append(i)

for i in reversed(idx_for_del):
    del numbers[i]

print(id(numbers))
print("Перемещённые элементы:", numbers)

