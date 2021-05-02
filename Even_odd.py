class Parity:
	even = []
	odd = []

	def add(self,value):
		if(value%2==0):
			Parity.even.append(value)
		else:
			Parity.odd.append(value)

	def print(self):

		print("Even List: ", Parity.even)
		print("Odd List: ", Parity.odd)


p = Parity()
p.add(12)
p.add(11)
p.add(13)
p.add(18)
p.print()