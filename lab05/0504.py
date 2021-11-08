from random import seed
from random import randint

n = 7
m = 10
a =[]

seed(320849)

for i in range(n):
	a.append([])
	for j in range(m):
		a[i].append(randint(0, 20))
	print(a[i])