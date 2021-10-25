a = 1
b = 1
c = 2
if a == b:
	if a == c:
		print('Wszystkie liczby, a, b, c, sa sobie rowne.')
	else:
		print('Liczby a i b sa rowne.')
else:
	if a == c:
		print('Liczby a i c sa rowne.')
	else:
		if b == c:
			print('Liczby b i c sa rowne.')
		else:
			print('Nie ma pary rownych liczb.')
