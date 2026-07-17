""" 03 Глубина вложенности списка

Напишите рекурсивную функцию, которая
- определяет максимальную глубину вложенности списка.

Функция должна проверять:
- Аргумент должен быть списком.
- Вложенные структуры, если они есть, также должны быть списками.
- Если данные не валидны необходимо выбрасывать исключение.

При вызове функции обработайте возможное исключение.

Данные:
nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]

Пример вывода:
Максимальная глубина: 5
"""

def max_depth(data):
    if not isinstance(data, list):
        raise TypeError("Аргумент должен быть списком.")

    if not data:
        return 1

    max_d = 0

    for item in data:
        if isinstance(item, list):
            depth = max_depth(item)
            if depth > max_d:
                max_d = depth
        elif isinstance(item, (dict, tuple, set)):
            raise TypeError(f"Вложенная структура {type(item).__name__} не является списком.")

    return 1 + max_d


nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]

try:
    result = max_depth(nested_list)
    print(f'Максимальная глубина: {result}')

except TypeError as e:
    print(f'Ошибка: {e}')

#  # 2 Вариант
# def max_depth(data):
#         # 1. Проверяем, что текущий аргумент является списком
#         if not isinstance(data, list):
#             raise TypeError("Аргумент должен быть списком.")
#
#         # Базовый случай: если список пустой, его глубина равна 1
#         if not data:
#             return 1
#
#         current_max = 0
#
#         for element in data:
#             # Если элемент является списком, уходим в рекурсию
#             if isinstance(element, list):
#                 depth = max_depth(element)
#                 if depth > current_max:
#                     current_max = depth
#             # 2. Валидация: если элемент — это другая структура (коллекция), но не список
#             elif isinstance(element, (tuple, set, dict)):
#                 raise TypeError(f"Вложенная структура {type(element).__name__} не является списком.")
#
#         # Прибавляем 1 (текущий уровень) к максимальной глубине вложенных списков
#         return 1 + current_max
#
#
#     # Данные для проверки
# nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]
#
# try:
#         # Вызов функции и вывод результата
#         result = max_depth(nested_list)
#         print(f"Максимальная глубина: {result}")
# except TypeError as e:
#         # Обработка ошибок валидации
#         print(f"Ошибка валидации данных: {e}")