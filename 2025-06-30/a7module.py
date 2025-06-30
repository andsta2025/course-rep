def ad(a,b):
    """ function that returns the sum of two numbers """
    return a + b
def sub(a,b):
    """ function that returns the difference of two numbers """
    return a - b
def mul(a,b):
    """ function that returns the product of two numbers """
    return a * b
def div(a,b):
    """ function that returns the quotient of two numbers """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
