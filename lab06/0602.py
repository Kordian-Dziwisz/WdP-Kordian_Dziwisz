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

userNum = int(input())
numSum = 0
numOfPrimes = 0
num = 1
while (numSum < userNum):
	if (isPrime(num)):
		numOfPrimes+=1
		numSum += num
	num += 1

print(numOfPrimes-1)