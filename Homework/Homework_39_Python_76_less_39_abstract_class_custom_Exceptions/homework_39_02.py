""" 02 Проверка размеров фигур

Доработайте фигуры:
Добавьте проверку в инстанцирование Circle и Rectangle,
чтобы значения были строго положительными.
Если передано отрицательное или нулевое значение,
выбрасывайте пользовательское исключение InvalidSizeError.
"""

from abc import ABC, abstractmethod
import math

class InvalidSizeError(Exception):
    pass

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        if radius < 0:
            raise InvalidSizeError(
                f"Значение radius={radius} должно быть положительным!"
            )

        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):

    def __init__(self, width, height):
        if width <= 0:
            raise InvalidSizeError(
                f"Значение width={width} должно быть положительным!"
            )

        if height <= 0:
            raise InvalidSizeError(
                f"Значение height={height} должно быть положительным!"
            )

        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


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
