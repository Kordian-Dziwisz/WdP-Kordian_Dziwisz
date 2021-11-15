def isPrime(num):
	import math
	if (num == 1):
		return False
	elif (num < 3):
		return True
	elif(num%2==0):
		return False
	else:
		for i in range(2, math.floor(math.sqrt(num))+1):
			# print(i)
			if(num%i==0):
				return False

for i in range(1, 100):
	if (isPrime(i)):
		if (isPrime(i + 2)):
			print(i, "i ", i+2)