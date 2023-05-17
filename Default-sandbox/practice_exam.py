# x = 5
# for i in range(x):
#     x = x + i
#     print(x, end=" ")

# s = "This string has words in it"
# words = s.split()
# for i, word in enumerate(words):
#     print(word[-1])

# class Arbitrary(object):
#     def __init__(self, data=1):
#         self.data = data
#
#     def getit(self):
#         return self.data * 2
#
#
# class Thing(Arbitrary):
#     def __init__(self, value=3):
#         super().__init__(value * 2)  # Pass on to parent constructor (data)
#
#
# a, b = Arbitrary(2), Thing()
# print(a.getit(), b.getit())

# data = [1, 2, 3, 4, 5]
# x = data.sort()  # None
# x = data[-1:0:-1]  # [5, 4, 3, 2]
# x = data[1:4:4]  # [2]
# x = sorted(data)[1:1]  # []
# print(x)

# text = 'O when THE Saints'
# parts = text.lower().split()
# for i, part in enumerate(sorted(parts)):
#     print(part, i)
# print(sorted(parts))

# class Building:
#     def __init__(self, name: str, maximum_occupancy: int):
#         self.name = name
#         self.maximum_occupancy = maximum_occupancy
#
#     def will_fit(self, number):
#         return number <= self.maximum_occupancy
#
#
# b = Building("Innovation Complex", 1200)
# result = b.will_fit(1201)
# print(result)

# string = "CP1404 is good"
# print(string[-1:0:-1])

# def main():
#     calories = [75, 65, 6175]
#     food = ["Egg", "Apple", "Carrot Cake"]
#     print(create_dictionary(food, calories))
#     # test_dict = dict(zip(food, calories))
#     # print(test_dict)
#
#
# def create_dictionary(food, calories):
# food_to_calories = {}  # FOR LOOP
# for item in range(len(food)):
#     key = food[item]
#     value = calories[item]
#     food_to_calories[key] = value
# return food_to_calories
#
# return dict(zip(food, calories))  # ZIP
# dictionary = {}
# for item in range(len(food)):
#     dictionary[food[item]] = calories[item]
# return dictionary


# main()

def main():
    for i in range(5):
        print(do_thing(i))


def do_thing(i):
    return i * "**"


main()
