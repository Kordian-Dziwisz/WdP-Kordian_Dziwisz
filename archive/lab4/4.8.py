print('Podaj wysokosc i dlugosc prostokata')
a = int(input())
b = int(input())
outStr=''
for i in range(a):
	for j in range(b):
		outStr+='X'
	print(outStr)
	outStr=''
