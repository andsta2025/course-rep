user_input = input("Enter numbers separated by space : ")
numbers = [int(num) for num in user_input.split()]
smallest = numbers[0]
largest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")
