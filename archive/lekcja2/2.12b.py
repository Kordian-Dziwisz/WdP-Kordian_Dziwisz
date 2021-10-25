a = 1
b = 1
c = 8
if a <= b <= c:
	minNum = a
elif a <= c <= b:
	minNum = a
elif b <= a <= c:
	minNum=b
elif b <= c <= a:
	minNum = b
elif c <= a <= b:
	minNum =c
elif c <= b <= a:
	minNum = c

print(minNum)