source = input("Enter the name of source file: ")
with open(source,'r') as f1:
	lines = f1.read()
	target = input('Enter the name of Target File:')
	with open(target,'w') as f2:
		f2.write(lines)