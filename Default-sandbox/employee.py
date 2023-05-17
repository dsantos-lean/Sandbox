from person import Person
from datetime import datetime


class Employee(Person):
    def __init__(self, name: str, date_of_birth: datetime.date, salary: float):
        super().__init__(name, date_of_birth)
        self.salary = salary
        print("Employee init")

    def __str__(self):
        return f"{super().__str__()} ${self.salary:.2f}"
