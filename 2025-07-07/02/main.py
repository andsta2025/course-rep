def devide_numbers(a, b):
    """
    Devide two numbers and return the result.
    try it, and if it fails, return an error message if an exception occurs
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
def main():
    """Let the user input two numbers and divide them"""
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = devide_numbers(a, b)
        print(f"The result of dividing {a} by {b} is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

