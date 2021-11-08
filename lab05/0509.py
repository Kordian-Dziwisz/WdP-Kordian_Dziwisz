from random import seed
from random import randint
seed(320849)

n = 3


A =[]
for i in range(n):
	A.append([])
	for j in range(n):
		A[i].append(randint(0, 20))
	print(A[i])
print('')


detA = 0

def calcSmallerM(M):
	smallerM = []
	for i in range(len(M) - 1):
			smallerM.append([])
			for j in range(len(M) - 1):
				smallerM[i].append(M[i][j])
	return smallerM

def calcDetM(M):
	if (len(M) == 1):
		# print(M)
		return M[0][0]
	else:
		detM = 0
		for i in range(len(M)):
			for j in range(len(M)):
				detM=pow(-1, i+1*j+1)*M[i][j]*calcDetM(calcSmallerM(M))
		return detM

print(calcDetM(A))
