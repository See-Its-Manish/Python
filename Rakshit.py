from multipledispatch import dispatch

class hello:

	@dispatch(int,int)
	def add(a,b):
		return(a+b)

	@dispatch(int,int,int)
	def add(a,b,c):
		return(a+b+c)