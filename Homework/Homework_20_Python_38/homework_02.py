""" 02 Фильтрация чисел по чётности

Напишите функцию filter_type, которая
- принимает первый аргумент ("even" или "odd")
- и произвольное количество чисел,
- возвращая только те, которые соответствуют фильтру.

Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
"""

def is_even(n):
    # Возвращаем TRUE если число чтное
    return n % 2 == 0

def is_odd(n):
    # Возвращаем TRUE если число НЕ четное
    return n % 2 != 0

def filter_numbers(filter_type, *numbers):
    # Если выбран фильтр четных чисел
    if filter_type == "even":
        # создаем список только из четных
        return [num for num in numbers if is_even(num)]
# Если выбран фильтр НЕ четных
    elif filter_type == "odd":
        # создаем список только из НЕ четных
        return [num for num in numbers if is_odd(num)]
    # Если фильтр указан не верно
    else:
        return "Некорректный фильтр"

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))   # [2, 4, 6]
print(filter_numbers("odd", 10, 15, 20, 25))      # [15, 25]
print(filter_numbers("prime", 2, 3, 5, 7))        # Некорректный фильтр