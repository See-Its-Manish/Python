l = [112,111,21,112,23,42,354,566]
oddsum=evensum=0
for i in range(len(l)):
	if(l[i]%2==0):
		evensum+=l[i]
	else:
		oddsum+=l[i]
print("Odd Sum: ",oddsum)
print("Even Sum: ",evensum)