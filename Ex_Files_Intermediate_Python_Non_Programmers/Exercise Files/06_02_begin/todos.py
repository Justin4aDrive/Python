import sys

file_name = "todo_data.txt"
todos = []

# Read File
try:
    file = open(file_name, "r")
    todos = file.readlines()
    file.close()
except:
    pass

print(todos)

# Add Todo

# Remove Todo

# Save File
file = open(file_name, "w")
file.writelines(todos)
file.close()

# Print List
print("\nHere's your ToDo list:\n")
print("1. Walk the Dog")
print("2. Buy Cheese")

# Print Commands
print("\n*******************************\n")
print(f"To view ToDos:\n{sys.argv[0]}")
print(f"\nTo add a ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")
