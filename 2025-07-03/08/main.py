class Vehicle:
    def start(self):
        print("The vehicle starts.")

    def stop(self):
        print("The vehicle stops.")

class Car(Vehicle):
    def start(self):
        print("The car starts with a roar.")

    def stop(self):
        print("The car stops smoothly.")

    def drive(self):
        print("The car is driving on the road.")

class Airplane(Vehicle):
    def start(self):
        print("The airplane starts its engines.")

    def stop(self):
        print("The airplane lands and stops.")

    def fly(self):
        print("The airplane is flying in the sky.")

class FlyingCar(Car, Airplane):
    def start(self):
        print("The flying car starts its engines and takes off.")

    def stop(self):
        print("The flying car lands and stops.")
    
    def fly(self):
        print("The flying car is flying in the sky like an airplane.")
    
    def drive(self):
        print("The flying car is driving on the road like a car.")

fcar = FlyingCar()

fcar.start()
fcar.drive()
fcar.fly()
fcar.stop()

print(isinstance(fcar, Car))
print(isinstance(fcar, Airplane))
print(isinstance(fcar, Vehicle))
