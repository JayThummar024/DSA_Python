
import math

a = [3,5,8,2,1,10,4]

########################################### Bubble sort ###########################################

# here we compare two adjcant elements and swap them as require...so after the first iteration the largest element will be at the last index , then we sort the ramaining elements untill the whole array is sorted


def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# print(bubbleSort(a))


######################################   Selection Sort   ################################################

# In this we divide the array in two part sorted and unsorted , Initially sorted part contain 0 elements
# then we find the minimum element in unsorted part of array and move that element to sorted part of array

# This algorithm is not suitable for large no of inputs , so only used when no. of inputs are less

def selectionSort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]
    return a

# print(selectionSort(a))


#################################################   Insertion sort ##########################################

# In this we divide the array in two part sorted and unsorted , Initially sorted part contain first element of given array and rest of the part is unsorted
# we loop through array and check the current element's position in sortd array

def insertionSort(a):
    for i in range(1, len(a)):
        current_ele = a[i]
        pos = i
        while pos > 0 and a[pos-1] > current_ele:
            a[pos] = a[pos-1]
            pos -= 1
        a[pos] = current_ele
    return a

# print(insertionSort(a))


########################################## Bucket sort ###########################################

# in this we create certain no. of buckets acc to formulae and then put every element of the array in the appropriate array using formulae ,then we sort all the bucket using any sorting algorithm and then we merge the buckets

def bucketSort(arr):
    noOfbuckets = round(math.sqrt(len(arr)))
    print(noOfbuckets)
    maxValue = max(arr)
    buckets = []

    for i in range(noOfbuckets):
        buckets.append([])

    for j in arr:
        bucketNo = math.ceil((j*noOfbuckets)/maxValue)
        buckets[bucketNo-1].append(j)

    for k in range(noOfbuckets):
        buckets[k] = insertionSort(buckets[k])

    k = 0
    for i in range(noOfbuckets):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

    return arr


# print(bucketSort(a))


############################################### merge sort #############################################

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



################################################ Quick sort ###############################################

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


quickSort(a, 0, len(a)-1)
print(a)








