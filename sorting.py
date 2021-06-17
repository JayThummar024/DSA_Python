
import math

a = [2, 5, 4, 1, 9, 6, 7, 8, 3]

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

#below implementationtakse O(n*log(n)) time and O(1) space complexity

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


