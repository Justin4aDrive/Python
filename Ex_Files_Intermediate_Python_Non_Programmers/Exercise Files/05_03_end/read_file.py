file = open("cheese.txt", "r")

# file_text = file.read()
# print(file_text)

# lines = file.readlines()
# print(lines)

for line in file:
    print(line)

file.close()

# Create a file numbers.txt that has a few lines of numbers.
# Multiply all the numbers together and print the result.

file = open("numbers.txt", "r")

total = 1
for line in file:
    try:
        number = float(line)
        total *= number
    except Exception as e:
        pass

print(total)

file.close()
