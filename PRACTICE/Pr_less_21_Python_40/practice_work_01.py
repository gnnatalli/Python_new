""" 01 Частотный анализ слов

Напишите программу, которая
- подсчитывает количество вхождений каждого слова в тексте.

Программа должна игнорировать регистр слов и символы . и ,.  (точки и запятые)

Данные:
text = "This is a test. This test is only a test."
Пример вывода:
{'this': 2, 'is': 2, 'a': 2, 'test': 3, 'only': 1}

"""

from collections import Counter

text = "This is a test. This test is only a test."
sample = {'this': 2, 'is': 2, 'a': 2, 'test': 3, 'only': 1}

def get_words_count(text):
    pass


print(get_words_count(text))
print(get_words_count(text) == sample)
# {'this': 2, 'is': 2, 'a': 2, 'test': 3, 'only': 1}
# True