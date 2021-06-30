# here we compare two adjcant elements and swap them as require...so after the first iteration the largest element will be at the last index , then we sort the ramaining elements untill the whole array is sorted


def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a