class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name
    def get_age(self) -> int:
        return self.__age
    def set_name(self, name: str) -> None:
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name = name
    def set_age(self, age: int) -> None:
        if age < 0:
            raise ValueError("Age must be non-negative")
        self.__age = age

person = Person("Jonas", 35)
print(f"Name: {person.get_name()}, Age: {person.get_age()}")

person.set_name("Julius")
person.set_age(37)

print(f"Updated Name: {person.get_name()}, Updated Age: {person.get_age()}")

