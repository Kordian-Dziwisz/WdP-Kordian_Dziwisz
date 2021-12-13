def permute(a, l, r):

    if l == r:
        print(a)

    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)

            if (a[i] == a[l])
            a[l], a[i] = a[i], a[l]


a = ['A', 'B', 'C', 'C']
permute(a, 0, len(a)-1)
