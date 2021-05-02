"""
class ---> Its a collection of data members and member functions/methods (C/C++/Java)
class --->  Its a blueprint of its instances or object. (Generalised)
"""
# Function -->  User Defined
# Constructor --> __init__
# Class ---> Blueprint
class Student:

	# Class Variable
	class_name = "CSE - A"

	def __init__(self, name, marks):
		self.name = name
		self.marks = marks
		print("Values are Set")

	def show(self):
		print("Name:",self.name)
		print("Marks",self.marks)
		print("Class:", Student.class_name,"\n")

# # Class Student object / Instance of class Student
s1 = Student("Mankaran",100)
s1.show()

s2 = Student("Ishan", 90)
s2.show()





	