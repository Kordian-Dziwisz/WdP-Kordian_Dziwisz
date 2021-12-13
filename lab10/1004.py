dict1 = {1: 10, 2: 7, 3: 8, 4: 15, 5: 14, 6: 3, 7: 2}


def bubbleSortDictonary(a):
    for i in range(1, len(a)):
        for j in range(1, len(a) - i + 1):
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
    return a


bubbleSortDictonary(dict1)
print(dict1)

dict2 = {8: 10, 9: 40, 10: 34, 11: 100}
dict1.update(dict2)
dict3 = dict1.copy()
print(dict3)

dict4 = {1: 10, 3: 50, 6: 4, 10: 2}
for i in range(1, len(dict3)):
    try:
        dict3[i] += dict4[i]
    except KeyError:
        False

print(dict3)
