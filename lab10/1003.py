import copy


def smallerM(m, r, c):
    del m[r]
    print(m)
    for i in m:
        print(c)
        del i[c]
    print(m)
    return m


def detA(m):
    if len(m) == 1:
        return m[0][0]
    else:
        det = 0
        for i in range(len(m)):
            det += m[0][i] * detA(smallerM(copy.copy(m), 0, i))
        return det


m = [[1, 2, 3], [2, 5, 3], [2, 9, 8]]

print(detA(m))
# smallerM(m, 0, 0)
