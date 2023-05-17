try:
    number = input("> ")
    print(int(number + 1))
except ValueError:
    print("Not a valid integer")
except TypeError:
    print("Invalid type of thing")
except:
    print("Some other exception happened")
else:
    print("Else")
print("Finished") 