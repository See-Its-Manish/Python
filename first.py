class Computer:
	 def __init__(self):
	 	self.__maxprice = 900

	 def sell(self):
	 	print("Selling Price: ", self.__maxprice)

	 def getMaxPrice(self):
	 	return self.__maxprice


c = Computer()
print(c.getMaxPrice())