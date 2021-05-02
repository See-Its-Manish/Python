"""
Q3. Write a program that has a class Circle .
Use a class variable to define the value of constant PI. 
Use this class variable to calculate are and circumference of a circle with specified radius.
"""

class Circle:
	pi = 3.1415

	def __init__(self,r):
		self.circum = 2*Circle.pi*r
		self.area = Circle.pi*(r**2)

	def show(self):
		print("Circumference:",self.circum)
		print("Area:",self.area)

c = Circle(4)
c.show()