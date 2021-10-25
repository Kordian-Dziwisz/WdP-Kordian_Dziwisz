s = 'programujemy w pythonie'
print(s)
print(len(s))
print(s[2:7])
print(s[-8:])
print(s[1])

s2 = s.upper()
print(s2)
s3 = s.lower()
print(s3)

r = 'Anna, Bartek, Celina, Dawid'
x1 = r.split(",")
print(x1)
r2 = r.replace(" ", "")
print(r2)
x1 = r2.split(",")
print(x1)
imie = "Jan"
nazwisko = 'Kowalski'
imnaz = imie + " " + nazwisko
print(imnaz)