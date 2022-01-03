# tworzenie
filePath = 'test.txt'
try:
    ioF = open(filePath, 'x')
except FileExistsError:
    print(f'file {filePath} already exists')

# zapisywanie
oS = ''
for i in range(100):
    oS += f'{i+1}\n'
ioF = open(filePath, 'w')
ioF.write(oS[:-1])


# zamkniecie
ioF.close()

# ponowne otwarcie
ioF = open(filePath, 'r')
iS = ioF.read()
iA = iS.split('\n')
oS = ''
for i in range(len(iA)):
    iA[i] = int(iA[i]) if int(iA[i]) % 2 else int(iA[i]) + 10
    oS += f'{iA[i]}\n'

ioF = open(filePath, 'w')
ioF.write(oS[:-1])


# otwarcie dla sprawedzenia wyniku
ioF = open(filePath, 'r')
iS = ioF.read()
print(iS)

ioF.close()
