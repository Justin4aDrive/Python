file = open("cheese.txt", "r")

#file_text = file.read()
#print(file_text)

#lines = file.readlines()
#print(lines)

for line in file:
    print(line)

file.close()


#create a file numbers.txt that has a few line of numbers
#multiply all the numbers together and print the result.

import sys
file = open("numbers.txt", "r")

total=1
for line in file:
    try:
        number = float(line)
        total *= number
    except Exception as e:
        print(e)
        sys.exit(1)

print(total)

file.close()