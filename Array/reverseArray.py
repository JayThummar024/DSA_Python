def reverseArr(arr , start ,end):
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start+=1
        end-=1
    return arr



def revArr(arr):
    return arr[::-1]