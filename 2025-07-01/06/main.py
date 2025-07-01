class Car:
    def __init__(self, make, model, year, color, kilometers):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.kilometers = kilometers

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Kilometers: {self.kilometers}")
    
    def __str__ (self):
        return f"{self.year} {self.color} {self.make} {self.model} with {self.kilometers} km"

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, color='{self.color}', kilometers={self.kilometers})"

car1 = Car("Toyota", "Corolla", 2020, "Red", 15000)
car2 = Car("Honda", "Civic", 2019, "Blue", 30000)
car3 = Car("Ford", "Focus", 2021, "Black", 10000)
car4 = Car("Tesla", "Model 3", 2022, "White", 5000)

print("All cars:")
car1.display_info()
print(str(car1))
print(repr(car1))
car2.display_info()
print(str(car2))
print(repr(car2))
car3.display_info()
print(str(car3))
print(repr(car3))
car4.display_info()
print(str(car4))
print(repr(car4))

cars = [car1, car2, car3, car4]

print()