class Animal:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(self.sound)

my_animal = Animal("Miau!")
my_animal.make_sound()
my_animal2 = Animal("Auu!")
my_animal2.make_sound()