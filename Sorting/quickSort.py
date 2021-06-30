# in this we we take a pivot element at random (preffered 1st or last) and then we have two more pointer left and right , we iterate through array and we place all the elements less than pivot to the left and all the element greater than pivot to the right , after this pivot element is at right position ad we do same operation to left side of pivot and right side of the pivot

def partition(arr , start , end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while arr[start] <= pivot and start < len(arr):
            start+=1

        while arr[end] > pivot:
            end-=1

        if start < end:
            arr[start] , arr[end] = arr[end] , arr[start]

    arr[pivot_index] , arr[end] = arr[end] , arr[pivot_index]
    return end

def quickSort(arr , start ,end):
    if start < end:
        pi = partition(a, start, end)
        quickSort(a, start, pi-1)
        quickSort(a, pi+1, end)