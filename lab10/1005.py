towar = [{'nazwa': 'banan', 'jednostka': 'kg', 'ilosc': 10, 'cena': 3},
         {'nazwa': 'jabłko', 'jednostka': 'kg', 'ilosc': 16, 'cena': 2.5},
         {'nazwa': 'mąka pszenna', 'jednostka': 'op.', 'ilosc': 30, 'cena': 2.5},
         {'nazwa': 'mydło', 'jednostka': 'szt.', 'ilosc': 6, 'cena': 1.5},
         {'nazwa': 'jogurt naturalny', 'jednostka': 'szt.', 'ilosc': 20, 'cena': 1.5},
         {'nazwa': 'papier toaletowy 8 rolek', 'jednostka': 'op.', 'ilosc': 10, 'cena': 9}]


def wyszukaj(towar, nazwa):
    for produkt in towar:
        if produkt['nazwa'] == nazwa:
            return produkt


def sumuj(towar, nazwa):
    for produkt in towar:
        if produkt['nazwa'] == nazwa:
            return produkt['ilosc']*produkt['cena']


print(sumuj(towar, 'banan'))


def sumujWszystko(towar):
    totalPrice = 0
    for produkt in towar:
        totalPrice += produkt['ilosc'] * produkt['cena']
    return totalPrice


print(sumujWszystko(towar))


def dodajTowar(towar, nazwa, jednostka, ilosc, cena):
    towar.append({'nazwa': nazwa,
                 'jednostka': jednostka, 'ilosc': ilosc, 'cena': cena})


dodajTowar(towar, 'Snickersy', 'szt.', 40, 2)
print(sumujWszystko(towar))


def aktualizujIlosc(towar, nazwa, ilosc):
    for produkt in towar:
        if produkt['nazwa'] == nazwa:
            produkt['ilosc'] = ilosc


print(wyszukaj(towar, 'banan'))
aktualizujIlosc(towar, 'banan', 35)
print(wyszukaj(towar, 'banan'))


def filtrJednostka(towar, jednostka):
    outArr = []
    for produkt in towar:
        if produkt['jednostka'] == jednostka:
            outArr.append(produkt)
    return outArr


print(filtrJednostka(towar, 'szt.'))
