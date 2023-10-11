#read

file = open("cheese.txt", "r")
lines = file.readlines()
file.close()

#edit
#lines = ["Hello\n", "My name is Justin."]

#lines.insert(0, "I like cheese.\n")

#lines[1] = "Hello friend!\n"

#lines[-1] = lines[-1] + "\n"
#lines.append("Have a great one!")

#overwrite
file = open("cheese.txt", "w")
file.writelines(lines)
file.close()

#multiple each of the numbers in numbers.txt by 2 and rewrite the file with tne new numbers
import sys

file = open("numbers.txt", "r")
lines = file.readlines()
file.close()

for x in range(len(lines)):
    try:
        number = float(lines[x]) * 2
        lines[x] = f"{number}\n"
    except Exception as e:
        print(e)
        sys.exit(1)

file = open("numbers.txt", "w")
file.writelines(lines)
file.close()