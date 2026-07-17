""" 01 Не уникальные числа

Напишите программу, которая
- находит все числа, встречающиеся более одного раза в списке,
- и выводит их в порядке убывания.

Данные:
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
Пример вывода:
Числа, встречающиеся более одного раза: [8, 7, 4, 3]
"""

numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]

# # решение через словарь
# count = {}
#
# # берем значение по ключу num, а если такого ключа нет то 0
# for num in numbers:
#     count[num] = count.get(num, 0) + 1
#
# duplicates = []
#
# for key, value in count.items():
#     if value > 1:
#         duplicates.append(key)
#
# duplicates.sort(reverse=True)
# print("Числа, встречающиеся более одного раза: ", duplicates)

# 2 решение

duplicates = []

# с count считаем сколько число встречается раз в списке и проверяем нет ли повторов
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
# сортируем по убыванию
duplicates.sort(reverse=True)

print("Числа, встречающиеся более одного раза: ", duplicates)