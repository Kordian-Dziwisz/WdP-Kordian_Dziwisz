from random import seed
from random import randint

n = 4
m = 4
a =[]

seed(320849)

for i in range(n):
	a.append([])
	for j in range(m):
		a[i].append(randint(0, 20))
	print(a[i])

squareSum = 0
for i in range(n):
	for j in range(i+1, m):
		squareSum += a[i][j]
print(squareSum)