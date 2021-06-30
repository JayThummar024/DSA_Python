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