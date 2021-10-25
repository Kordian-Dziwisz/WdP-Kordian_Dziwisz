a = 12
b = 20
c = 12
possible = True
ostrokatny = False
rozwartokatny = False
prostokatny = False

#check if possible
if (a >= b):
	if (a >= c):
		# a is max
		longest = a
		if (a > b + c):
			possible = False
			print('to nie sa boki trojkata')
	else:
		# c is max
		longest = c
		if c > a + b:
			possible = False
			print('to nie sa boki trojkata')
else:
	if (b >= c):
		# b is max
		longest = b
		if (b > a + c):
			possible = False
			print('to nie sa boki trojkata')
	else:
		# c is max
		longest = c
		if c > a + b:
			possible = False
			print('to nie sa boki trojkata')

# check if rozwartokatny/prostokatny/ostrokatny
if (possible):
	if (longest == a):
		if a * a == b * b * 2:
			prostokatny = True
		elif a * a > b * b * 2:
			rozwartokatny = True
		else:
			ostrokatny = True
	elif (longest == b):
		if b*b == a*a*2:
			prostokatny = True
		elif b * b > a * a * 2:
			rozwartokatny = True
		else:
			ostrokatny = True
	else:
		if c*c == a*a*2:
			prostokatny = True
		elif c*c > a*a*2:
			rozwartokatny = True
		else:
			ostrokatny = True

#check if rownoboczny/rownoramienny/roznoboczny and print
if(possible):
	if a == b == c:
		print('trojkat ostrokatny rownoboczny')
	elif a == b or a==c or c==b:
		if (ostrokatny):
			print('trojkat ostrokatny rownoramienny')
		if(prostokatny):
			print('trojkat prostokatny rownoramienny')
		if(rozwartokatny):
			print('trojkat rozwartokatny rownoramienny')
	else:
		if (ostrokatny):
			print('trojkat ostrokatny roznoramienny')
		if(prostokatny):
			print('trojkat prostokatny roznoramienny')
		if(rozwartokatny):
			print('trojkat rozwartokatny roznoramienny')