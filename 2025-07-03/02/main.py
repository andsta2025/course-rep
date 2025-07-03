class Animal:
    def speak(self):
        return "I don't know what sound I make"
    
class Dog(Animal):
    def speak(self):
        return "Au!"
    
class Cat(Animal):
    def speak(self):
        return "Miau!"
    

dog = Dog()
cat = Cat()

print(dog.speak())  
print(cat.speak())  

