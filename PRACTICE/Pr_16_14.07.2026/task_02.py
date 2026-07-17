"""
2. Ограничение с указанием длины строки

Доработайте декоратор limit_output, чтобы он принимал параметр
max_len — максимальная длина строки.

Пример применения:
@limit_output(26)
def get_text():
    return "Это очень длинный текст, который нужно обрезать."

Пример вывода:
Это очень длинный текст...
"""
def limit_output(max_len=20):
    def decorator(func):
        def wrapper(*args, **kwargs):
            long_text = func(*args, **kwargs)
            if len(long_text) > max_len:
                return long_text[:max_len - 3] + "..."
            return long_text
        return wrapper
    return decorator


@limit_output(26)
def get_text():
    return "Это очень длинный текст, который нужно обрезать."


print(get_text())

# Это очень длинный текст...