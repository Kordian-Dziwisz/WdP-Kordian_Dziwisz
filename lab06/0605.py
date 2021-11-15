from random import seed
from random import randint
seed(320849)
num = randint(0, 100)
won = False
while won == False:
	userNum = int(input())
	if userNum == num:
		won = True
	else:
		if (userNum > num):
			print('liczba jest za duza')
		else:
			print('liczba jest za mala')

print('wou win!')