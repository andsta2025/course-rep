import math1

x = int(input("Enter first number: "))
if x < 0:
    raise ValueError("First number must be non-negative")       
y = int(input("Enter second number: "))
if y < 0:
    raise ValueError("Second number must be non-negative")

print(f"{x} + {y} = {math1.add(x, y)}")
print(f"{x} - {y} = {math1.subtract(x, y)}")
print(f"{x} * {y} = {math1.multiply(x, y)}")
print(f"{x} / {y} = {math1.divide(x, y)}")