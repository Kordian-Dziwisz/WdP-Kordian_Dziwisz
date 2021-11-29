def binary(n, prevBits=[]):
	print(n)
	if n % 2:
		prevBits.append(1)
	else:
		prevBits.append(0)
	if n // 2 > 0:
		return binary(n//2, prevBits)
	else:
		prevBits.reverse()
		return prevBits

print(binary(3))