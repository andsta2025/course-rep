class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name: str, age: int, grade: int):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self) -> str:
        return f"{super().introduce()} My grade is {self.grade}."
    
Person1 = Person("Alice", 30)
Student1 = Student("Bob", 20, 10)
Student2 = Student("Charlie", 22, 12)

print(Person1.introduce())
print(Student1.introduce())
print(Student2.introduce())