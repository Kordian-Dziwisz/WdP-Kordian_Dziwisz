import math
print('podaj a')
a = input()
print('podaj b')
b = input()
print('podaj kąt alfa w stopniach')
alfa = input()
c = float(a) * float(b) * math.sin(math.radians(float(alfa))) / 2
print(f'pole trójkąta to: {c}')