print("Enter the age: ", end="")
age = input()
age = int(age)
if age <= 0:
    print("Enter valid age")
    exit(0)
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to Vote")
