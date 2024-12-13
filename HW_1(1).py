from abc import ABC, abstractmethod
import math

# Абстрактный класс Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Класс-наследник Circle для круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Класс-наследник Rectangle для прямоугольника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Пример использования:
circle = Circle(5)  # Радиус круга = 5
rectangle = Rectangle(4, 7)  # Стороны прямоугольника = 4 и 7

print(f"Площадь круга: {circle.area()}")
print(f"Площадь прямоугольника: {rectangle.area()}")
