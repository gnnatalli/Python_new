"""
1. Ограничение длины строки

Создайте декоратор limit_output(max_len=20), который обрезает строку,
возвращаемую функцией, до max_len символов (включая многоточие).
Если строка длиннее max_len, то она обрезается до выбранного лимита
и завершается троеточием ..., входящим в этот лимит.
Если нет - остаётся как есть

Пример применения:
@limit_output
def get_text():
    return "Это очень длинный текст, который нужно обрезать."

Пример вывода:
Это очень длинный...
"""
def limit_output(func):
    def wrapper(*args, **kwargs):
        max_len = 20
        long_text = func(*args, **kwargs)
        if len(long_text) > max_len:
            return long_text[:max_len - 3] +"..."
        return long_text
    return wrapper


@limit_output
def get_text1():
    return "Это очень длинный текст, который нужно обрезать."

@limit_output
def get_text2():
    return "Это не очень длинный"

print(get_text1())
print(get_text2())

# Это очень длинный...
# Это не очень длинный