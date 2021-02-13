# Program to find greatest among three numbers.
n1 = input("Enter First Number: ")
n2 = input("Enter Second Number: ")
n3 = input("Enter Third Number: ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 >= n2 and n1 >= n3:
    print("Greatest of three is ", n1)
elif n2 >= n1 and n2 >= n3:
    print("Greatest of three is ", n2)
else:
    print("Greatest of three is ", n3)
