import math
x = 3
isPrime = True
if (x == 1):
	isPrime = False
elif(x%2==0):
	isPrime = False
elif(x>3):
	for i in range(2, math.floor(math.sqrt(x))+1):
		# print(i)
		if(x%i==0):
			isPrime = False
			print("liczba nie jest pierwsza")
			break

if (isPrime):
	print("liczba jest pierwsza")
else:
	print('liczba nie jest pierwsza')
