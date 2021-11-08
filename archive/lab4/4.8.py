print('Podaj wysokosc i dlugosc prostokata')
a = int(input())
b = int(input())
outStr = ''
if (a > 0 and b > 0):
	for i in range(a):
		for j in range(b):
			outStr+='X'
		print(outStr)
		outStr=''
