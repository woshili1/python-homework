import re

def test():
	a = '''<div id ="111" class="hehe">abc</div>'''
	#b = r'<div *.?>(*.?)</div>'
	b=r'<div .*>(.*)</div>'
	c=re.findall(b,a)
	print(c)

if __name__ == "__main__":
	#url='''http://flights.ctrip.com/booking/bjs-xmn-day-1.html?ddate1=2017-02-07'''
	test()