# To count tht number of type of numbers in list

l = [1,1,2,2,4,5,5,9]

count = 1

for i in range(len(l)-1):
	if(l[i]!=l[i+1]):
		count+=1

print("Answer: ",count)