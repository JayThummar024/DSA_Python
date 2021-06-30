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