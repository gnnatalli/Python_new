""" 02 Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28
"""


def sum_digits_non_tail(lst):
    total = 0

    for item in lst:
        if isinstance(item, list):
            total += sum_digits_non_tail(item)
        else:
            total += item

    return total


def sum_digits_tail(lst, acc=0):
    if not lst:
        return acc

    first = lst[0]
    rest = lst[1:]

    if isinstance(first, list):
        acc = sum_digits_tail(first, acc)
    else:
        acc += first

    return sum_digits_tail(rest, acc)

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

print(sum_digits_tail(nested_numbers))       # 28
print(sum_digits_non_tail(nested_numbers))   # 28