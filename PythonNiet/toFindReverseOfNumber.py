# Program to Find the reverse of a number.

n = input("Enter a number: ")
n = int(n)


rev = 0
while n > 0:
    rev = (rev * 10) + int(n % 10)
    n = n // 10


print("Reverse of Given Number: ", rev)
