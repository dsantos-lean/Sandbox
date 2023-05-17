vowels = "aeiouAEUIOU"
number_of_letters = 0
number_of_vowels = 0
name = input("Name: ")
for letter in name:
    number_of_letters += 1
    if letter in vowels:
        number_of_vowels += 1
# print(f"Out of {number_of_letters} letters, {name} has {number_of_vowels} vowels")
# print("Out of", number_of_letters, "letters,", name, "has", number_of_vowels, "vowels")
print("Out of {} letters, {} has {} vowels".format(number_of_letters, name, number_of_vowels)) # String formatting