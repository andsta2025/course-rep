def apply_function(numbers, func):
    """ 'func' to each number in the list 'numbers', param func: Function to apply to each number """
    return [func(num) for num in numbers]   

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   
    def square(x):
        return x * x
    
    squared_numbers = apply_function(numbers, square)
    
    print("Originals:", numbers)
    print("Squared:", squared_numbers)