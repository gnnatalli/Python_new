""" 02 Зеркальное подмножество

Напишите программу, которая
- проверяет, являются ли элементы одного из множеств подмножеством другого.

В случае положительного ответа возвращает разницу между двумя множествами.

Проверить необходимо в обе стороны.

Данные:
set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}

Пример вывода:
Подмножество: True
Разница: {2, 3, 6}
=====================
Данные:
set1 = {2, 3, 4, 5, 6}
set2 = {4, 7}

Пример вывода:
Подмножество: False
"""

# set1 = {2, 3, 4, 5, 6}
# set2 = {4, 5}
#
# if set2.issubset(set1):
#     print("Подмножество: True")
#
#     difference = set1 - set2
#     print("Разница", difference)
#
# elif set1.issubset(set2):
#     print("Подмножество: True")
#
#     difference = set1 - set2
#     print("Разница: ", difference)
#
# else:
#     print("Подмножество: False")


set1 = {2, 3, 4, 5, 6}
set2 = {4, 7}

if set2.issubset(set1):
    print("Подмножество: True")

    difference = set1 - set2
    print("Разница", difference)

elif set1.issubset(set2):
    print("Подмножество: True")

    difference = set1 - set2
    print("Разница: ", difference)

else:
    print("Подмножеcтво: False")