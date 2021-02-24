"""
Sum of Series :  1^2 + 3^2 + 5^2 + ----- + n^2
n---> odd
"""
n = int(input("Enter the nth number: "))
sumOfSeries = (n*(2*n+1)*(2*n-1))/3
print("Sum of the Series: ",sumOfSeries)

