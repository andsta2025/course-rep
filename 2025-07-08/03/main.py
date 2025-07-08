def decorator_with_message(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Message: {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_message("Executing the function with a custom message")
def example_function_with_message(n):
    return f"Function executed with input: {n}"
if __name__ == "__main__":
    
    user_input = input("Please enter a message: ")
    print(example_function_with_message(user_input))
  