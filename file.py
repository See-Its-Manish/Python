try:
	n = int(input("Enter number to be divided: "))
	divisor = int(input("Enter Divisor: "))
	div = n/divisor
	print(div)
except ZeroDivisionError:
	print("Can't Divide by Zero")