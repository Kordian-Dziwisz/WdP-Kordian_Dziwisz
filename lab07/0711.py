def odleglosc(p1, p2):
	import math
	return math.sqrt(abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2)

def calcSlope(p1, p2):
	return (p2[1]-p1[1])/(p2[0]-p1[0])

def naJednejLinii(p1, p2, p3):
	return p1[0]==p2[0] and p2[0]==p3[0] or p1[1]==p2[1] and p2[1]==p3[1] or calcSlope(p1, p2) == calcSlope(p2, p3) and calcSlope(p2, p3) == calcSlope(p1, p3)


def obwodTrojkata(p1, p2, p3):
	if (naJednejLinii(p1, p2, p3)):
		return False
	return odleglosc(p1, p2) + odleglosc(p2, p3) + odleglosc(p1, p3)

print(obwodTrojkata([-2, 0], [2, 2], [4, 3]))