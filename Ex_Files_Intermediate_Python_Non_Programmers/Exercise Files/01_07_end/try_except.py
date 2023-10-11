
print("before")

try:
    #4 / 0
    print(age)
except NameError as e:
    print("this was  a name issue")
    print(e)
except ZeroDivisionError:
    print("Can't divide by 0")
except Exception as e:
    print("Something went wrong")

class CheeseError(Exception):
    pass

def upper_fun(word):
    if len(word) <= 0:
        raise CheeseError("The word has to have at least one letter!")
    return word.upper()

#print(upper_fun(""))

print("after")

# Find something I haven't mentioned that will throw
# an exception in Python and put it in a try, except
try:
    int("nick")
except:
    print("OOPS")
