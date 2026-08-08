"""01 Фигуры и площади

Создайте абстрактный класс Shape.
В классе должен быть метод get_area(), который возвращает площадь фигуры.
Реализуйте два класса:
- Circle, который принимает радиус.
- Rectangle, который принимает ширину и высоту.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Площадь круга:", circle.get_area())
    print("Площадь прямоугольника:", rectangle.get_area())


    # Площадь круга: 78.53981633974483
    # Площадь прямоугольника: 24
