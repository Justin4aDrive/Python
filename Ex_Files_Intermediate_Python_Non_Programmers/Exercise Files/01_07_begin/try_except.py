
print("before")

try:
    #4 / 0
    print(age)
except NameError as e:
    print("this was a name issue")
    print(e)
except ZeroDivisionError:
    print("can't device by zero")
except Exception as e:
    print("Somethign went wrong.")

class CheeseError(Exception):
    pass

def upper_fun(word):
    if len(word) <= 0:
        raise CheeseError("Word has to have at least one letter!")
    return word.upper()

print(upper_fun("a"))

try:
    print(random.randint(1,10))
except NameError as e:
    print(e)

try:
    int("Nick")
except ValueError as e:
    print(e)

print("after")


