def findchar(string,char):
	for i ,key in enumerate(string):
		if(key==char):
			return i
	return -1
def rfindchar(string,char):
	location = -1
	strtemp = reversed(string)
	for i ,key in enumerate(strtemp):
		if(key==char):
			location = i
	return len(string) -location-1
def subchar(string,old,new):
	temp = ""
	for key in string:
		if key==old:
			temp = temp+new
		temp = temp+key
	return temp
if __name__ == '__main__':
	str = "abcdqwewqewq.^&*ds"
	strkey=input("input")
	old = input("old")
	new = input("new")
	print(findchar(str,strkey))	
	print(rfindchar(str,strkey))
	print(subchar(str,old,new))		