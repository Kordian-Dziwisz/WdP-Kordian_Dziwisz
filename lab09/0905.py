a = 0
b = 12


def NWD(a, b):
    if a > 0 and b > 0:
        while b > 0:
          	print(a, b)
            tmp = a
            a = b
            b = tmp
            # print(a, b)
            b = b % a
            # print(a, b)
        return a
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return 0


def NWDRec(a, b):
    if b != 0:
        return NWDRec(b, a % b)
    return a


# def NWDRec(a, b):


print(NWD(a, b))
print(NWDRec(a, b))
