""" 10 Развернуть слова

Напишите программу, которая
- делает реверс каждого слово в строке,
- сохраняя при этом порядок слов.
(т.е. реверсирует слова, а не текст)

Пример вывода:
Строка: Python is fun
Результат: nohtyP si nuf
"""

text = "Python is fun"
words = text.split()
result = []

for word in words:
    result += [word[::-1]]

print("Строка: ", text)
print("Результат: ", "_".join(result))

