""" 02 Функция mdc (my deepcopy)

Реализуйте аналог deepcopy() с помощью рекурсии.
Не забудьте проверить, чтобы изменения в копии не затронули оригинал.

Данные:
original_data = [
    [1, 2, 3],                 # Вложенный список
    (4, [5, 6], {7, 8}),       # Тюпл с вложенными структурами
    {"a": 9, "b": [10, 11]},   # Словарь со списком
    "Hello",                   # Строка
    [12, (13, 14)],            # Список с тюплом
    15.5,                      # Число с плавающей точкой
    5                          # Целое число
]
Пример вывода:
Исходный: [[1, 2, 3], (4, [0, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]
Копия:    [[1, 2, 3], (4, [5, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]

"""

def mdc(original_data):

    if isinstance(original_data,list):
        return [mdc(item) for item in original_data]

    elif isinstance(original_data, dict):
        return {key: mdc(value) for key, value in original_data.items()}

    elif isinstance(original_data, tuple):
        return tuple(mdc(item) for item in original_data)

    elif isinstance(original_data, set):
        return {mdc(item) for item in original_data}

    return original_data


od = [[1, 2, 3], (4, [0, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]

od_copy = mdc(od)
print(od_copy)
print(od == od_copy)  # True

# Меняем исходный список
od[0][1] = 5
print(od == od_copy)  # False