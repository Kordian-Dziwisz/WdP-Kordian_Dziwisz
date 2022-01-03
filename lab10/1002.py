def subsets(a, i, sub):
    if i == len(a):
        print(sub)
    else:
        subsets(a, i + 1, sub + [a[i]])
        subsets(a, i + 1, sub + [])


a = ['A', 'B', 'C']
subsets(a, 0, [])
