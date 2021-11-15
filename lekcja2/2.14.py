import math
a = 1
b = -2
c = 1

delta = b * b - 4 * a * c
if c == 0 and (b == 0 or a == 0):
	print('rownanie ma nieskonczenie wiele rozwiazan')
else:
	if a != 0:
		if delta < 0:
			print('rownanie nie ma rozwiazan:')
		elif delta == 0:
			print('rownanie ma 1 rozwiazanie: ', -b/(2*a))
		else:
			print('rownanie ma 2 rozwiazania: ', (-b + math.sqrt(delta)) / (2 * a), ' i ', (-b - math.sqrt(delta)) / (2 * a))
	else:
		if b!=0:
			print('rownanie ma 1 rozwiazanie: ', -c/b)
		else:
			print('rownanie nie ma rozwiazan')