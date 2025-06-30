def print_args(*args):
    """ function that prints all arguments passed to it """
    for arg in args:
        print(arg)

print("Test 1:")
print_args("Utenos", "Vilniaus", "Smetoniška")
print("\nTest 2:")
print_args(1, 2, 3, 4, 5)
print("\nTest 3:")
print_args("Hello", "World", 123, 456.789)
print("\nTest 4:")
print_args("single argument")
print("\nTest 5:")
print_args()  # No arg
