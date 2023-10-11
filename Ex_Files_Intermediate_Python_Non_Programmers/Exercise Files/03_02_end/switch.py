# Requires Python 3.10

direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "east":
        print("Right")
    case "west":
        print("Left")
    case _:
        print("Not a valid direction")

# Create a switch for a number

floor_number = 4

match floor_number:
    case 4:
        print("Unlucky in Japan")
    case 13:
        print("Unlucky in America")
    case _:
        print("No issuses with this floor number :D")
