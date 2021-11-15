fa = 1
fb = 1
temp = 0
for i in range(30):
	temp = fa
	fa += fb
	fb = temp
	print(fa)
