from random import seed
from random import randint
seed(320849)

n = 3
m = 5
A =[]


for i in range(n):
	A.append([])
	for j in range(m):
		A[i].append(randint(0, 20))
	print(A[i])
print('')

m = 5
p = 4
B =[]


for i in range(m):
	B.append([])
	for j in range(p):
		B[i].append(randint(0, 20))
	print(B[i])
print('')

C = []
for i in range(n):
	C.append([])
	for j in range(p):

		cElement = 0
		for k in range(m):
			cElement += A[i][k] * B[k][j]
		C[i].append(cElement)
	print(C[i])