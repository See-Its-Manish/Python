n=int(input("Enter a number: "))
sumOfDigits=0
reverse=0
while(n>0):
	r=n%10
	sumOfDigits+=r
	reverse=(reverse*10)+r
	n=n//10

print("Sum of Digits:", sumOfDigits)
print("Reverse of number:", reverse)
