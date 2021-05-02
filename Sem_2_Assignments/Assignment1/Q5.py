"""
Q5.Write a class that stores a string and all its status details such as 
number of uppercase characters , vowels ,consonants ,space etc.
"""

class String:

	def __init__(self, s):
		self.s = s
		self.upper=self.lower=self.digit=self.space=0
		self.consonants=self.vowels=0

	def calculate(self):

		for ch in self.s:
			if(ch.isalpha()):
				if(ch.isupper()):
					self.upper+=1
				elif(ch.islower()):
					self.lower+=1
				vowels = ['A','E','I','O','U','a','e','i','o','u']
				if(ch in vowels):
					self.vowels+=1
				else:
					self.consonants+=1

			else:
				if(ch.isdigit()):
					self.digit+=1
				elif(ch.isspace()):
					self.space+=1


	def show(self):
		print("UpperCase  :",self.upper)
		print("LowerCase  :",self.lower)
		print("consonants :",self.consonants)
		print("Vowels     :", self.vowels)
		print("digit      :", self.digit)
		print("Space      :", self.space)

s1 = String("Manish Sharma 2002")
s1.calculate()
s1.show()





