beers = ["Vilniaus", "Exstra", "Dundulio", "Corona", "Heineken"]
print("The original list of beers is:", beers)

# Add a new beer to the list
new_beer = input("Enter the name of a new beer to add: ")
beers.append(new_beer)
print("Updated list of beers:", beers)
# Remove a beer from the list
beer_to_remove = input("Enter the name of a beer to remove: ")
if beer_to_remove in beers:
    beers.remove(beer_to_remove)
    print(f"{beer_to_remove} has been removed from the list.")
else:
    print(f"{beer_to_remove} there is no such beer in the list.")
# print("Print elements of the list:", beers {0:3})  # Print the first three beers
print("Print element of the list:", beers [3])  # Print beers from index
