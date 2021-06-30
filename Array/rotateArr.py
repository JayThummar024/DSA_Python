def rotate( arr, n):
    last = arr[-1]
    arr.pop()
    arr.insert(0,last)
    return arr