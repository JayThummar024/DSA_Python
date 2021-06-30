def negSort(a):
    for i in range(len(a)):
        if a[i] > 0:
            a.append(a[i])
            a.remove(a[i])
    return a