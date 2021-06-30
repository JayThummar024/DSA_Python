def maxProd(arr):
    max = 1
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i]*arr[j] > max:
                max = arr[i]*arr[j]
    return max 

def mProd(arr):
    arr.sort()
    return arr[-1]*arr[-2]

print(mProd([0,1,2,5,2,8,9]))