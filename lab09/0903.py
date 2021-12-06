def askForNum():
	print('podaj liczbe')
	num = float(input())
	return num

a = []
for i in range(0, 10):
	a.append(askForNum())

# a = [12, 53, 64, 23, 54, 2, 53, 128]
def bubbleSort(a):
	for i in range(len(a)-1):
		for j in range(len(a) - 1 - i):
			if a[j] > a[j + 1]:
				tmp = a[j]
				a[j] = a[j + 1]
				a[j + 1] = tmp
	return a

print(bubbleSort(a))