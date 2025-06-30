def sort_by_length(strings):
    """Sorts a list of strings by their length."""
    return sorted(strings, key=len)

list_1 = ["apple", "banana", "kiwi", "cherry", "blueberry"]
list_2 = ["short", "longer", "longest", "tiny"]
list_3 = ["a", "ab", "abc", "abcd", "abcde"]
list_4 = ["one", "two", "three", "four", "five"]

print(sort_by_length(list_1))  
print(sort_by_length(list_2))  
print(sort_by_length(list_3))  
print(sort_by_length(list_4))  
