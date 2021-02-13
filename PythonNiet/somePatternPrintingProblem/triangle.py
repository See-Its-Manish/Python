# Program to print Triangle pattern
n = int(input("Enter the height of Triangle: "))  # Will Print Triangle of n height

noOfSpaces = n - 1  # Setting the value of noOfSpaces for First Line
noOfStars = 1  # Setting the value of noOfStars for First Line

for i in range(1, n + 1):  # This Loop will change the lines and set the values -----Loop 1
    # of noOfSpaces and noOfStars for a next Line.

    # After these two loops are for single line(Spaces+Stars)

    for j in range(1, noOfSpaces + 1):  # This Will Print Spaces Staring from n-1 to 0--Loop(2)
        print(" ", end="")  # Printing Spaces for Single line --(Loop 2)
    for k in range(1, noOfStars + 1):  # This will Print Stars staring from 1 till 2n-1 (Inc. by 2)
        print("*", end="")  # Print Stars

    print()  # Changing Line ----(Loop 1)
    noOfSpaces -= 1  # Decreasing no. of Spaces to be printed in next line--(Loop 1)
    noOfStars += 2  # Increasing no. of Stars to Printed in Next Line--(Loop 2)
