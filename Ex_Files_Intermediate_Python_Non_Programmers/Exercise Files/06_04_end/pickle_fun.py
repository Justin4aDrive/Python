import pickle

class ToDo:
	def __init__(self, title, important, category = "Normal"):
		self.title = title
		self.important = important
		self.category = category

todos = [ToDo("Walk Dog", True), ToDo("Eat Cheese", False), ToDo("Learn Python", True, category = "Work")]


age = [23,523,5,324,632,5,35]

file = open("text.txt", "wb")
pickle.dump(todos, file)
file.close()

file = open("text.txt", "rb")
new_todos = pickle.load(file)
file.close()

print(new_todos)
