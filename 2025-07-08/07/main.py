def memorize(func):
    cache = {}  # dictionary to store cached results

    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for args {args}")
            return cache[args]
        else:
            print(f"Cache miss for args {args}")
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

# Example usage:
@memorize
def slow_function(x, y):
    print(f"Computing slow_function({x}, {y})...")
    return x + y

# Test calls
print(slow_function(2, 3))  # Computes and caches
print(slow_function(2, 3))  # Returns cached result
print(slow_function(4, 5))  # Computes and caches
print(slow_function(4, 5))  # Returns cached result