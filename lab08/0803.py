def tiles(n, k):
	if n == 1:
		return n * k
	else:
		return (2 * (n-1) + 1) * k + tiles(n - 1, k)

print(tiles(1, 2))
print(tiles(2, 2))
print(tiles(3, 6))
print(tiles(4, 2))
print(tiles(5, 2))