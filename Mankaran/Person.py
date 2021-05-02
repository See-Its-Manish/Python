class Person:
	category = "Homo Sapiens" # Class Variable

	def __init__(self, name, DOB, Age):

		# name, DOB, Age ---->  Variables local to __init__ function ---> function
		
		# Instance variable
		self.name = name + " Sharma"
		self.DOB  = DOB
		self.Age = Age


	def show(self):
		print("Name:", self.name)
		print("DOB:", self.DOB)
		print("Age:", self.Age)
		print("Category:",Person.category )

p1 = Person("Manish", "19-9-2020", 1)
p1.show()