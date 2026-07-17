""" 02 Реверс строки

Напишите рекурсивную функцию, которая
- переворачивает строку.

Если передан не строковый тип, выбросить исключение.
При вызове функции обработайте возможное исключение.

Данные:
text = "recursion"
Пример вывода:
noisrucer
"""

def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError('Аргумент должен быть строкой.')

    if len(s) <= 1:
        return s

    return s[-1] + reverse_string(s[:-1])
# Проверка
# Ok
text = 'recursion'
# Err1
# text = ['a', 'b', 'c']
# Err2
# text = 123
try:
    result = reverse_string(text)
    print(result)
except TypeError as e:
    print(f'Ошибка валидации данных: {e}')
