"""
3. Кеширование результатов
Создайте декоратор cache, который сохраняет результат вызова функции
для каждого набора аргументов.
Если функция вызывается повторно с теми же аргументами —
возвращается сохранённый результат.

Пример применения:
@cache
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
Результат из кеша:
6
"""
def cache(func):
    res_cache = {}

    def wrapper(*args, **kwargs):
        if args in res_cache:
            return f"Результат из кеша:\n {res_cache[args]}"

        res_cache[args] = func(*args)
        return res_cache[args]

    return wrapper


@cache
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b

print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(2, 3))

# Вычисляем 2 * 3:
# 6
# Результат из кеша:
# 6
# Вычисляем 4 * 5:
# 20
# Результат из кеша:
# 6