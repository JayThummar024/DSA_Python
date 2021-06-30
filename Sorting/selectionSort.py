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