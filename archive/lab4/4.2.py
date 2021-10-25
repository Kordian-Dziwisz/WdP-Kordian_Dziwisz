waga = 75
wzrost = 180

s = "Jan Kowalski (waga: {}, wzrost: {})"
s = s.format(waga, wzrost)
print(s)

waga_txt = str(waga)
wzrost_txt = str(wzrost)
s = "Jan Kowalski (waga: " + waga_txt + ', wzrost: ' + wzrost_txt + ')'
print(s)