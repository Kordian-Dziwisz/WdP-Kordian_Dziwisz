def odleglosc(p1, p2):
	import math
	return math.sqrt(abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2)

print(odleglosc([7.5, -8], [-2, 0]))