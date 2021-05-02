"""
Q2. Write a program with class Employee that keeps a track of the number of employees
in an organization and also stores their name , designation  and salary details.
"""

class Employee:

	employee_count = 0

	def __init__(self, name, desig, sal):
		self.name = name
		self.desig = desig
		self.sal = sal
		Employee.employee_count += 1

	def display(self):
		print("Name of Employee:", self.name)
		print("Designation:", self.desig)
		print("Salary:",self.sal,"\n")

	def print_count(self):
		print("Number of Employees:", Employee.employee_count,"\n")

Ramesh = Employee("Ramesh", "SDE-I",100000)
Suresh = Employee("Suresh", "SDE-II",150000)
Ramesh.display()
Ramesh.print_count()