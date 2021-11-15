print('Podaj imiona rozdzielone przecinkami')
inStr = input()
strArr = inStr.split(',')
outStr = ''
for i in strArr:
	if i[-1]=='a':
		outStr += i + ', '
print(outStr[0:-2])