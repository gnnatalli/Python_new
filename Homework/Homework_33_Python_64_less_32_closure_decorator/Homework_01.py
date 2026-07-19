""" 01 Среднее время выполнения

Создайте декоратор measure_time, который
- измеряет и выводит среднее время выполнения функции за 5 вызовов.

Функция может быть любой:
    например, сортировка списка, чтение из файла или расчёты.

Пример применения:
@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 5 вызовов: 0.21 секунд
Результат: 49999995000000

"""

import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        times = []
        result = None

        for _ in range(5):
            start = time.time()

            result = func(*args, **kwargs)

            end = time.time()
            times.append(end - start)

        average_time = sum(times) / 5
        print(f"Среднее время выполнения для 5 вызовов: {average_time:.2f} секунд")
        print(f"Результат: {result}")

        return result

    return wrapper

@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


compute()

# Среднее время выполнения для 5 вызовов: 0.47 секунд
# 49999995000000