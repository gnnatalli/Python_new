"""
2.2. Фильтрация списка строк по длине

Доработайте функцию так, чтобы можно было передавать значение минимальной длины слов, которые нужно оставить.
words = ["hi", "Hello", "a", "python", "Ok"]
min_len = 2

Пример вывода:
['hi', 'Hello', 'python', 'Ok']
"""

def filter_by_predicate(
    words: list[str],
    min_len: int
) -> list[str]:
    return [word for word in words if len(words) >= min_len]

words = ["hi", "Hello", "a", "python", "Ok"]

print(filter_by_predicate(words, min_len=2))