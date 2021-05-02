class String:

	def __init__(self, str):
		self.str = str

		self.UC = self.LC = self.Num = self.Spaces = 0
		self.consonents = self.vowels = 0

	def string_Analysis(self):

		vowels = ['A','E','I','O','U','a','e','i','o','u']
		for i in self.str:

			if(i.isalpha()):

				if(i in vowels):
					self.vowels += 1
				else:
					self.consonents += 1

			if(i.isupper()):
				self.UC += 1
			elif(i.islower()):
				self.LC += 1
			elif(i.isdigit()):
				self.Num += 1
			elif(i == " "):
				self.Spaces += 1

	def get_string_analysis(self):
		print("No of UpperCase: ", self.UC)
		print("No of LowerCase: ", self.LC)
		print("No of Digits: ", self.Num)
		print("No of Consonents: ", self.consonents)
		print("No of Vowels:", self.vowels)


s1 = String("Riya Bisht 300")
s1.string_Analysis()
s1.get_string_analysis()

