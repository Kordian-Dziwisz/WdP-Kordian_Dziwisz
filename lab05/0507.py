A = [[4, 0, 8], [1, 0, 7], [12, -2, 18], [12,77, 88]]

B = []

for i in range(len(A[0])):
	B.append([])
	for j in range(len(A)):
		B[i].append(A[j][i])
	print(B[i])