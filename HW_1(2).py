from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    position: str
    salary: float

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)


employee1 = Employee("Nikolay", 34, "PM", 800000)
employee2 = Employee("Mr.Bean", 23, "QA", 120000)

employee1.increase_salary(10)
employee2.increase_salary(15)

print(employee1)
print(employee2)
