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
		if (isPrime):
			return True

for i in range(2, 200):
	if (isPrime(i)):
		print(i)