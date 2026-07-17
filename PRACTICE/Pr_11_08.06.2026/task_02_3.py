""" 2.3. Фильтрация списка строк по критерию

Доработайте функцию так, чтобы можно было передавать критерии отбора слов, которые нужно оставить.
(то есть аргументом должен стать callable-объект)
Например:
- слова, начинаются с заглавной буквы
- слова из одного символа
- слова начинаются и заканчиваются одной буквой, независимо от регистра

words = ["hi", "Hello", "a", "python", "Ok", "Radar"]
Пример вывода:
['Hello', 'Ok', 'Radar']
['a']
['a', 'Radar']
"""

from typing import Callable

def filter_words(
        words: list[str],
        predicate: Callable[[list[str]], bool]
) -> list[str]:
    return [word for word in words if predicate(word)]

words = ["hi", "Hello", "a", "python", "Ok", "Radar"]

print(
    filter_words(
        words,
        lambda word: word[0].isupper()
    )
)

print(
    filter_words(
        words,
        lambda word: len(word) == 1
    )
)

print(
    filter_words(
        words,
        lambda word: word[0].lower() == word[-1].lower()
    )
)