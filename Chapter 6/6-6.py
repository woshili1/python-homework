def mystrip(text):
	for char in text:
		if(char==" "):
			textlen = len(text)
			text =text[1:textlen]
		else:
			break
	print(text)
	for char in text[::-1]:
		if(char==" "):
			text =text[1:len(text)]
		else:
			break
	print(text)
	return text[::-1]
if __name__ == '__main__':
	text = input("input your text with blank")
	print(mystrip(text))
