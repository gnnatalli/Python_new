"""04 Группы слов

Напишите программу, которая
- принимает список строк
- и группирует их по общей длине в обратном порядке.

Группы должны быть отсортированы по убыванию длины строки,
а внутри каждой группы строки должны быть отсортированы в алфавитном порядке.

Данные:
words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]

Пример вывода:
Группы слов:
[['banana', 'cherry'], ['apple', 'grape', 'melon'], ['kiwi', 'pear']]
"""
# Итоговый список для сравнения с результатом:
sample = [['banana', 'cherry'], ['apple', 'grape', 'melon'], ['kiwi', 'pear']]


words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]

sample = [['banana', 'cherry'], ['apple', 'grape', 'melon'], ['kiwi', 'pear']]


words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]

words.sort(key=len, reverse=True)

groups = []

for word in words:
    added = False

    for group in groups:
        if len(group[0]) == len(word):
            group.append(word)
            added = True
            break

    if not added:
        groups.append([word])

for group in groups:
    group.sort()

print(groups)