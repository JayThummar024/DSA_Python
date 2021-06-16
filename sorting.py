
a=[2,5,4,1,9,6,7,8,0,3]

########################################### Bubble sort ###########################################

# here we compare two adjcant elements and swap them as require...so after the first iteration the largest element will be at the last index , then we sort the ramaining elements untill the whole array is sorted

def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j] ,a[j+1] = a[j+1] , a[j]
    return a
        
# print(bubbleSort(a))



######################################   Selection Sort   ################################################

# In this we divide the array in two part sorted and unsorted , Initially sorted part contain 0 elements
# then we find the minimum element in unsorted part of array and move that element to sorted part of array

# This algorithm is not suitable for large no of inputs , so only used when no. of inputs are less

def selectionSort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1 , len(a)):
            if a[j] < a[min_idx] :
                min_idx = j
        a[min_idx] , a[i] = a[i] , a[min_idx]
    return a

# print(selectionSort(a))



#################################################   Insertion sort ##########################################

# In this we divide the array in two part sorted and unsorted , Initially sorted part contain first element of given array and rest of the part is unsorted
# we loop through array and check the current element's position in sortd array 

def insertionSort(a):
    for i in range(1,len(a)):
        current_ele = a[i]
        pos = i
        while pos>0 and a[pos-1] > current_ele:
            a[pos] = a[pos-1]
            pos-=1
        a[pos] = current_ele
    return a

# print(insertionSort(a))


