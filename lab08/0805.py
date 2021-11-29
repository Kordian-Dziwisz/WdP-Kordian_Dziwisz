def isPrime(num):
	import math
	if (num == 1):
		return True
	elif (num < 3):
		return True
	elif(num%2==0):
		return False
	else:
		for i in range(3, math.floor(math.sqrt(num))+1):
			# print(i)
			if(num%i==0):
				return False
	return True

def factorial(n, prevFactors=[]):
	import math
	if (isPrime(n)):
		prevFactors.append(n)
		return prevFactors
	if (not n % 2):
		prevFactors.append(2)
		return factorial(n/2, prevFactors)
	for i in range(3, math.sqrt(n), 2):
		if (isPrime(i) and not n % i):
			prevFactors.append(i)
			return factorial(n / i, prevFactors)

print(factorial(64))
print(factorial(3))
