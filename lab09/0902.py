def askForNum():
	print('podaj liczbe')
	num = float(input())
	return num

a = []
for i in range(0, 10):
	a.append(askForNum())

maxNum = a[0]
for num in a:
	if num > maxNum:
		maxNum = num

print(a)
print(maxNum)