print('Podaj imie i nazwisko:')
im_naz = input()
strArr = im_naz.split(' ')
print(f"{strArr[0]} {strArr[1].upper()}")