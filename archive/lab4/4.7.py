print('Podaj bok trojkata')
n = int(input())
outStr = ''
for i in range(n+1):
	for j in range(i):
		outStr += 'X'
	print(outStr)
	outStr=''