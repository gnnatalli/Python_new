""" 02 Список уникальных слов

Дан текст. Программа должна:
Разбить текст на слова.
Создать список уникальных слов в алфавитном порядке (не учитывая регистр).
Вывести количество уникальных слов.

Данные:
text = "Python is a great programming language. Python is popular and powerful."

Пример вывода:
Количество уникальных слов: 9
Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming', 'python']
"""

text = "Python is a great programming language. Python is popular and powerful."
format_text = text.replace(".", "").lower().split()
uniq_text = []
for word in format_text:
    if word not in uniq_text:
        uniq_text.append(word)
uniq_text.sort()
print("Количество уникальных слов:", len(uniq_text))
print("Уникальные слова:", uniq_text)
