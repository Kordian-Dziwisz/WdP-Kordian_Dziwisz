n = 8
def sumUpToNRec(n):
	if n == 1:
		return 1
	else:
		return sumUpToNRec(n - 1) + n

def sumUpToN(n):
	sumN = 0
	for i in range(n+1):
		sumN += i
	return sumN

print(sumUpToN(n))
print(sumUpToNRec(n))