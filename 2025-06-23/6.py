# Create two sets with some elements
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date", "elderberry"}

# Print the original sets
print("Set A:", set_a)
print("Set B:", set_b)

# Add an element to set_a
set_a.add("fig")
print("\nSet A after adding 'fig':", set_a)

# Remove an element from set_b
set_b.remove("date")
print("Set B after removing 'date':", set_b)

# Perform union of set_a and set_b
union_set = set_a.union(set_b)
print("\nUnion of A and B:", union_set)

# Perform intersection of set_a and set_b
intersection_set = set_a.intersection(set_b)
print("Intersection of A and B:", intersection_set)

# Perform difference of set_a and set_b (A - B)
difference_set = set_a.difference(set_b)
print("Difference of A and B (A - B):", difference_set)