ch = input("Enter a character:")

vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

if((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')):	# ch.isupper()
	if(ch in vowel):
		print("Vowel")
	else:
		print("Consonent")
else:
	print("Not an alphabet")
# elif(ch >= 'a' and ch <= 'z'):	# ch.lower()
# 	print("LC")
# elif(ch >= '0' and ch <= '9'):	# ch.isdigit()
# 	print("Digit")
# else:
# 	print("Special character")
# if(ch in vowel):
# 	print("Vowel")

