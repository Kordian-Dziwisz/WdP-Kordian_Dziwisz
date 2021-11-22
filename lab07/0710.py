def odleglosc(p1, p2):
	import math
	return math.sqrt(abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2)

def obwodTrojkata(p1, p2, p3):
	return odleglosc(p1, p2)+odleglosc(p2, p3)+odleglosc(p1,p3)

print(obwodTrojkata([7.5, -8], [-2, 0], [7, 12]))