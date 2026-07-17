"""01 Сумма чисел списка

Напишите рекурсивную функцию, которая
- вычисляет сумму всех чисел в списке.

Функция должна проверять:
- Аргумент должен быть списком.
- Все элементы списка должны быть числами.

Если данные не валидны необходимо выбрасывать исключение.
При вызове функции обработайте возможное исключение.

Данные:
numbers = [1, 2, 3, 4, 5]
Пример вывода:
15
"""

def recursive_sum(lst):
    if not isinstance(lst, list):
        raise TypeError("Аргумент должен быть списком.")
    if not lst:
        return 0
    first = lst[0]

    if not isinstance(first, (int, float)):
        raise TypeError(f"Элемент '{first}' не является числом.")

    return first + recursive_sum(lst[1:])

# numbers = [1, 2, 'f', 4, 5]
# numbers = [1, 2, [3, 4], 5]
# numbers = [1, 2, 3, 4, 5]
# numbers = 5
numbers = 'Строка'
try:
    result = recursive_sum(numbers)
    print(result)
except TypeError as e:
    print(f"Ошибка валидации данных: {e}")


