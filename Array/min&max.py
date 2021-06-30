def minmax(arr):
    min = 0
    max = 0
    if len(arr) == 1:
        min = arr[0]
        max = arr[0]
    if len(arr) == 2 and arr[0] > arr[1]:
        min = arr[1]
        max = arr[0]
    if len(arr) == 2 and arr[0] < arr[1]:
        min = arr[0]
        max = arr[1]
    if len(arr) > 2:
        min = arr[0]
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
            if arr[i] > max:
                max = arr[i]
    return {"min" : min , "max":max}