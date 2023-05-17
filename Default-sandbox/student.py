from person import Person
from datetime import datetime


class Student(Person):
    def __init__(self, name: str, date_of_birth: datetime.date, course: str):
        # takes kwargs into this constructor
        Person.__init__(self, name, date_of_birth)
        self.name = name
        self.date_of_birth = date_of_birth
        # super().__init__(**kwargs)  # Parent class requirements, kwargs passed on to parent constructor
        self.course = course
        print("Student init")

    def __repr__(self):
        return str(vars(self))


if __name__ == '__main__':
    lean = Student(name="Lean", date_of_birth=datetime(2020, 2, 14), course="BIT")
    datetime(1990, 12, 5), "BIT"
    print(lean)
    print(lean.age())
