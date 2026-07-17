"""
4. Кеш с ограничением по размеру
Доработайте декоратор cache, чтобы он:
 - Принимал параметр max_size, ограничивающий количество сохранённых записей.
 - При превышении max_size — удалял самую старую запись из кеша.

Пример применения:
@cache(max_size=2)
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b

Пример вывода:
print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(2, 3))

Вычисляем 2 * 3:
6
Результат из кеша:
6
Вычисляем 4 * 5:
20
Вычисляем 6 * 7:
42
Вычисляем 2 * 3:
6
"""
from collections import OrderedDict

def cache(max_size=10):
    def decorator(func):
        res_cache = OrderedDict()

        def wrapper(*args):
            if args in res_cache:
                return f"Peзультат из кеша:\n{res_cache[args]}"

            res_cache[args] = func(*args)
            if len(res_cache) >= max_size:
                # Удаляем самый старый элемент
                res_cache.popitem(last=False)
            return res_cache[args]
        return wrapper
    return decorator


@cache(max_size=2)
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b


print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(5, 6))
print(multiply(2, 3))

# Вычисляем 2 * 3:
# 6
# Результат из кеша:
# 6
# Вычисляем 4 * 5:
# 20
# Результат из кеша:
# 6