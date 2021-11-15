arr = [3, 9, -7, 2, 0, 89, 8]
maxNum = arr[0]
minNum = arr[0]
for i in arr:
	if i > maxNum:
		maxNum=i
	elif i < minNum:
		minNum = i
print(maxNum)
print(minNum)