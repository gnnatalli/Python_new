""" 4. Сортировка списка по длине

Отсортируйте список слов по длине, используя параметр.

ВАЖНО: Обратите внимание на порядок отсортированных строк в примере:
Использована двух-уровневая сортировка:
 - прямая по длине слова;
 - и обратная по алфавиту.

Данные:
words = ["apple", "banana", "kiwi", "grape"]
print(sort_by_length(words))
Пример вывода:
['kiwi', 'grape', "apple", 'banana']
"""
# 1 вариант
# def sort_by_length(words):
#     return sorted(words, key=lambda w: (len(w), -ord(w[0])))

# 2 вариант
def sort_by_length(words):
    words_sorted = sorted(words, reverse=True)

    return sorted(words_sorted, key=len)



sample = ['kiwi', 'grape', "apple", 'banana']
words = ["apple", "banana", "kiwi", "grape"]

result = sort_by_length(words)
print(result)
print(result == sample)