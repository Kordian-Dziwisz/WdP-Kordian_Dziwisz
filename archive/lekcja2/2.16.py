import math
a = 1298830
if (a <= 99):
	print('bledna liczba')
else:
	print('Cyfra jednosci: ', a % 10)
	print('Cyfra dziesiatek: ', (a%100-a%10)/10)
	print('Cyfra setek: ', (a % 1000 - a % 100) / 100)
