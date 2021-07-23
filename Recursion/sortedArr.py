# check if the array is sorted or not


def sorted(arr):
    if len(arr)==1: 
        return 1

    if arr:
        if arr[0] < arr[1]: 
            arr.pop(0)
            return sorted(arr)
        else:
            return 0
        

print(sorted([1,2,3,4,5,6,9,8,7]))
    

    