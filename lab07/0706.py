def dom(levels=1, arg='x'):
	for i in range(levels):
		print(10*arg)
		print(3 * arg + 4 * ' ' + 3 * arg)
		print(3 * arg + 4 * ' ' + 3 * arg)
		print(10*arg)


def dach(arg='x'):
	print(4*' '+2*arg)
	print(3*' '+4*arg)
	print(2*' '+6*arg)
	print(1*' '+8*arg)
	print(10*arg)

dach('^')
dom(4, '#')