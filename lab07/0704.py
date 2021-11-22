def powitaj(imie = 'b/d'):
	print('czesc' + imie + '!')

def sumuj(a=0, b=0):
	print('suma', a, ' i ', b, ' to ', a + b)

powitaj()
powitaj('jan')
powitaj('anna')
sumuj()
sumuj(b=9)
sumuj(a=8)
sumuj(-4, 5)
sumuj(10, 300)