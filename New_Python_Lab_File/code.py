s = input("Enter a number: ")
print(type(s))
n = 0
for i in range(len(s)):
	n = n*10 + ord(s[i]) - ord("0")
print(n,type(n))
