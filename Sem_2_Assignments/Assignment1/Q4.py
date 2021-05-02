"""
Q4. Write a program that has a class student that stores roll number, name
and marks(in three subjects) of the students. Display the information(roll number,
name and total marks)stored about the student.
"""

class Student:

	def __init__(self, roll, name, marks):
		self.roll = roll
		self.name = name
		self.marks = marks
		self.total = 0
		for i in marks:
			self.total += i


	def show(self):
		print("Roll Numeber:",self.roll)
		print("Name of Student:", self.name)
		print("Total of marks in 3 Subjects:",self.total,'\n')

Ramesh = Student(1,"Ramesh", [90,90,90])
Mahesh = Student(2,"Mahesh", [90,98,89])
Ramesh.show()