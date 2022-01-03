def gcd(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return a
    elif b == 0:
        return b
    else:
        if a % b > 0:
            r = a % b
            a = b
            b = r
            return gcd(a, b)
        else:
            return b


def sqrt(n, a=0, b=0):
    if n == 1:
        return 1
    if b == 0 and a == 0:
        b = n // 2 + 1
        a = 1
    if ((a + b) // 2) ** 2 > n:
        b = (a + b) // 2
    else:
        a = (a + b) // 2
    return sqrt(n, a, b) if b - a > 1 else a


def toBin(n, arr=0):
    if arr == 0:
        arr = []
    arr.append(int(n % 2))
    if n > 1:
        return toBin(n//2, arr)
    else:
        arr.reverse()
        return arr


dictonary = {'name': {'name': 'hello'}}


while 1:
    num = int(input())
    print(sqrt(num))
    print(toBin(num))
    print(dictonary['name']['name'])
