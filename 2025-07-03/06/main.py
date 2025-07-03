class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    def work(self) -> str:
        return f"{self.name} is working."
    def get_salary(self) -> float:
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):    
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department
    def work(self) -> str:
        return f"{self.name} is managing the {self.department} department."
    def conduct_meeting(self) -> str:
        return f"{self.name} is conducting a meeting in the {self.department} department."
    def get_salary(self) -> float:
        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

class Engineer(Employee):
    def __init__(self, name: str, salary: float, specialization: str):
        super().__init__(name, salary)
        self.specialization = specialization
    def work(self) -> str:
        return f"{self.name} is engineering in the field of {self.specialization}."
    def design(self) -> str:
        return f"{self.name} is designing a new project in {self.specialization}."
    def get_salary(self) -> float:
        return f"Name: {self.name}, Salary: {self.salary}, Specialization: {self.specialization}"

class Intern(Employee):
    def __init__(self, name: str, salary: float, mentor: str):
        super().__init__(name, salary)
        self.mentor = mentor
    def work(self) -> str:
        return f"{self.name} is interning under {self.mentor}."
    def learn(self) -> str:
        return f"{self.name} is learning from {self.mentor}."
    def get_salary(self) -> float:
        return f"Name: {self.name}, Salary: {self.salary}, Mentor: {self.mentor}"
    

emp = Employee("Alice", 50000)
mgr = Manager("Bob", 80000, "Sales")
eng = Engineer("Charlie", 70000, "Software")
intn = Intern("David", 30000, "Eve")        

print(emp.work())

print(mgr.work())
print(mgr.conduct_meeting())
print(mgr.get_salary())

print(eng.work())
print(eng.design())
print(eng.get_salary())

print(intn.work())
print(intn.learn())
print(intn.get_salary())

print(emp.get_salary())
print(mgr.get_salary())
print(eng.get_salary())
print(intn.get_salary())

print(f"Manager {mgr.name} has a salary of {mgr.salary} and manages the {mgr.department} department.")
print(f"Engineer {eng.name} has a salary of {eng.salary} and specializes in {eng.specialization}.")
print(f"Intern {intn.name} has a salary of {intn.salary} and is mentored by {intn.mentor}.")
print(f"Employee {emp.name} has a salary of {emp.salary}.")
 
