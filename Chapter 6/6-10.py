def reverse(words):
	temp = ""
	for i in words:
		if(i.isalpha()):
			print(i)
			if(i.isupper()):
				print("before lower")
				i = i.lower()
				print("after lower",i)
			else:
				print("before upper")
				i = i.upper()
				print("after upper",i)
		temp = temp + i
	return temp

if __name__ == '__main__':
	str = "Mr.Lee"
	print(reverse(str))
