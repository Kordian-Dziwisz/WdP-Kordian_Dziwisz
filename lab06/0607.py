num = 16
binNum = []
while (num != 0):
	if (num % 2):
		binNum.append(1)
		num = int(num / 2)
	else:
		binNum.append(0)
		num = num/2
out = ''
for i in range(len(binNum)):
	out+=str(binNum[-i-1])
print(out)