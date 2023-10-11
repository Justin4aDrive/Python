



























class ToDo:
	def __init__(self, title, important, category = "Normal"):
		self.title = title
		self.important = important
		self.category = category


todos = [ToDo("Walk Dog", True), ToDo("Eat Cheese", False), ToDo("Learn Python", True, category = "Work")]
