from datetime import datetime


class Person:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth
        print("Person init")

    def __repr__(self):
        date_string = datetime.strftime(self.date_of_birth, "%d/%m/%Y")
        return f"{self.name} ({date_string})"

    def age(self):
        return int((datetime.now() - self.date_of_birth).days / 365.2425)


if __name__ == '__main__':
    ben = Person("Ben", datetime(2020, 2, 14))
    print(ben)
    print(f"{ben.name} is {ben.age()}")
