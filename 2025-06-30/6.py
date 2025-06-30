def find_index_in_list(lst, value):
    """Find the index of a value in a list, or return -1 if not found."""
    try:
        return lst.index(value)
    except ValueError:
        return -1
    
print(find_index_in_list([1, 2, 3, 4, 5], 3)) 
print(find_index_in_list([1, 2, 3, 4, 5], 6)) 
print(find_index_in_list(['apple', 'banana', 'cherry'], 'banana')) 
print(find_index_in_list(['apple', 'banana', 'cherry'], 'orange')) 
print(find_index_in_list([], 1)) 
print(find_index_in_list([1, 2, 3, 4, 5], 1))  
print(find_index_in_list([1, 2, 3, 4, 5], 5))  


