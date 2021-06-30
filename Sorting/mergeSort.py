# in this we divide array in half untill we have all the elements seperated then we merge them into acending order so the final array will be sorted

#below implementationtakse O(n*log(n)) time and O(n) space complexity

def merge_sorted_arr(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k =0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

    
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    merge_sorted_arr(left, right, arr)