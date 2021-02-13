ch=str(input("Enter a character: "))
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z') ):
	if(ch=='a'or ch=='e'or ch=='i' or ch=='o' or ch=='u'):
		print("Vowel")
	elif(ch=='A'or ch=='E'or ch=='I' or ch=='O' or ch=='U'):
		print("Vowel")
	else:
		print("Consonent")
else:
	print("Not an Alphabet")