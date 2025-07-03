import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

widht = 5.0
height = 10.0
radius = 3.0

print(f"Circle with radius {radius} has area: {math.pi * radius ** 2}")
print(f"Rectangle with width {widht} and height {height} has area: {widht * height}")

