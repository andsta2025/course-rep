class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

re1 = Rectangle(2, 20)
re2 = Rectangle(1, 5)
re3 = Rectangle(7, 15.5)

print(f"Area of re1: {re1.area()}, Perimeter of re1: {re1.perimeter()}")
print(f"Area of re2: {re2.area()}, Perimeter of re2: {re2.perimeter()}")
print(f"Area of re3: {re3.area()}, Perimeter of re3: {re3.perimeter()}")

