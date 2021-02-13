def Print(args, *vartuple):
	print(args)
	for var in vartuple:
		print(var, end=" ")
	return

Print(1,2,3,44,55)