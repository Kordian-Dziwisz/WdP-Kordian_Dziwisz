inStr = input()
strArr = inStr.split(" ")
for i in range(len(strArr)):
	strArr[i] = float(strArr[i])
if (strArr[0] > 0 and strArr[1] > 0):
	print(f'Pole prostokata p={strArr[0]*strArr[1]}, a obwod L={(strArr[0]+strArr[1])*2}')
else:
	print('Nieprawidlowe dane')
