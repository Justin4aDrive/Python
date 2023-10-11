direction = input("Which direction, please?").lower()

match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "east":
        print("Left")
    case "west":
        print("Right")
    case _:
        print("Not a valid direction; please try North, South, East, or West.")


number=3

match number:
    case 1:
        print("That is the loneliest number.")
    case 2:
        print("Can be as bad as 1.")
    case 3:
        print("It's a party.")
    case 4:
        print("We have some pairs.")
    case 5:
        print("Who'd the odd one out?")
    case _:
        print("Please try again with 1, 2, 3, 4, or 5.")
