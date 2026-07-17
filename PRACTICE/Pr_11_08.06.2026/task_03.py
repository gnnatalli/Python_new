""" 3. Агрегирование списка

Вычислите произведение всех элементов списка с помощью функции высшего порядка.

Данные:
numbers = [1, 2, 3, 4, 5]
Пример вывода:
120
"""


from functools import reduce

def product(numbers: list[int]) -> list[int]:
    return reduce(lambda a, b: a * b, numbers)
    pass

sample = 120
numbers = [1, 2, 3, 4, 5]

result = product(numbers)
print(result)
print(result == sample)
