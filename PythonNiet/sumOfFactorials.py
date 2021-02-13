# Print the sum of the series: 1! + 2! + 3! + ------ + n!

n=int(input("Enter a number: "))
product = 1;
sumOfSeries=0
i=1
while(n!=0): 
	product*=i
	sumOfSeries+=product
	n-=1 
	i+=1

print("Sum of the series: ", sumOfSeries)