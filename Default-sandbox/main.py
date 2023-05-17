from datetime import datetime
from person import Person
from student import Student
from employee import Employee


def main():
    p1 = Person("Jane", datetime(1999, 2, 14))
    print(p1)
    print(p1.age())
    s1 = Student("Jerry", datetime(2004, 2, 14), "BIT")
    print(s1)
    print(s1.age())
    e1 = Employee("Jack", datetime(1900, 5, 30), 500)
    print(e1)
    people = [p1, s1, e1]
    for person in people:
        print(person.age())


main()
