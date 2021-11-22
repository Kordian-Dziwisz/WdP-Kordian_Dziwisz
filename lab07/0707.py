def szukajWLiscie(lista, a):
	instances = 0
	for el in lista:
		if el == a:
			instances += 1
	return instances


print(szukajWLiscie([4, 0, 8, 9,  8,  'a', 0], 0))