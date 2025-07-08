import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        print(f"Arguments: {args}, {kwargs}")
        # Removed erroneous reference to 'n' and 'time.seep'
        # print(f"Total: {end_time - start_time + time.seep(n):.4f} seconds")
        return result
    return wrapper

@timing_decorator
def example_function(n):
   time.sleep(3)  # Simulating a delay
   return f"Function completed with input: {n}"

print(example_function(2))
print(example_function(5))
print(example_function(7))