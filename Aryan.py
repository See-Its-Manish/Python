# f = open("Lela.txt", "w")
# f.writelines("Helllo BroManish")
# f.writelines("hello Py")
# f.close()


a = 12
b =0

try:
	print(a/b)
except:
	print("exception", )

l = [i for i in range(1,41) if(i%2!=0)]
print(l)


s="NITIN"
rev =""
for i in range(len(s)-1,-1,-1):
	rev += s[i]

if(rev==s):
	print("Pallindrome")
else:
	print("Not Pallindrome")


l = []