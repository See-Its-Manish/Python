n = int(input("Enter a number: "))

k = 1
k = int(k)
for i in range(1, n+1):
    for j in range(1, i+1):
        print(k, end="")

        k += 1
    print()