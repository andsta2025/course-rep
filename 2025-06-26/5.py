calctome = input("Input operation (+,-,*,/): ")
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
if calctome == '+':
    result = num1 + num2
elif calctome == '-':
    result = num1 - num2
elif calctome == '*':
    result = num1 * num2
elif calctome == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is imposiiiiiblleee"
print(result)