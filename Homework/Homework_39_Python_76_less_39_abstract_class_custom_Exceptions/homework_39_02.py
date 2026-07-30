""" 02 Проверка размеров фигур

Доработайте фигуры:
Добавьте проверку в инстанцирование Circle и Rectangle,
чтобы значения были строго положительными.
Если передано отрицательное или нулевое значение,
выбрасывайте пользовательское исключение InvalidSizeError.
"""


class Shape():
    pass


class Circle():
    pass


class Rectangle():
    pass


if __name__ == "__main__":
    try:
        c = Circle(-5)
    except InvalidSizeError as e:
        print("Ошибка:", e)

    try:
        r = Rectangle(3, 0)
    except InvalidSizeError as e:
        print("Ошибка:", e)


# Ошибка: Значение radius=-5 должно быть положительным!
# Ошибка: Значение height=0 должно быть положительным!
