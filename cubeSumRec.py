# 1^3 + 2^3 + ----- + n^3 Using Recursive Function
def func(a):
	if(a==1):
		return 1
	sumOfSeries =func(a-1) + a**3
	return(sumOfSeries)

print("sumOfSeries:", func(5))