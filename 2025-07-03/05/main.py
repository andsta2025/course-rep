import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

widht = 5.0
height = 10.0
radius = 3.0

print(f"Circle with radius {radius} has area: {math.pi * radius ** 2}")
print(f"Rectangle with width {widht} and height {height} has area: {widht * height}")
print(f"Circle with radius {radius} has perimeter: {Circle(radius).perimeter()}")
print(f"Rectangle with width {widht} and height {height} has perimeter: {Rectangle(widht, height).perimeter()}")
