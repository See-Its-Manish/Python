"""
Q1. Write a program that uses class to store the name and marks of students .
Use list to store the marks in three subjects.
"""

class Student:

	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

	def show(self):
		print("Name of Student:", self.name)
		print("Marks in 3 Subject:", self.marks,"\n")


Manish = Student("Manish", [85,91,99] )
Manish.show()