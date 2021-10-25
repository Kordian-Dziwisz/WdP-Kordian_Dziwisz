a = 1
b = 2
c = 8
if (a <= b):
	minNum = a
	if (c <= a):
		minNum=c
else:
	if (c <= b):
		minNum = c
	else:
		minNum = b
print(minNum)