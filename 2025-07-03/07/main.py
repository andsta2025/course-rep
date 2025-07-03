class Vehicle:
    def start(self):
        print("Vehicle started.")        
    def stop(self):
        print("Vehicle stopped.")

class Car(Vehicle):
    def start(self):
        print("Car started and the car engine roars to life.")
        
    def stop(self):
        print("Car stopped and the car engine shuts off.")

class Truck(Vehicle):
    def start(self):
        print("Truck started.")
        
    def stop(self):
        print("Truck stopped.")

class Motorcycle(Vehicle):
    def start(self):
        print("The motorcycle revs up.")
        
    def stop(self):
        print("The motorcycle stops and the engine cuts off.")

car = Car()
truck = Truck()
motorcycle = Motorcycle()

car.start()
car.stop()

truck.start()
truck.stop()

motorcycle.start()
motorcycle.stop()   


