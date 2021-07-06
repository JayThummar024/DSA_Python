def minimumSwaps(arr):
    ans =0
    for i in range(len(arr)):
        if arr[i] != i+1:
            for j in range(i+1 ,len(arr)):
                if i+1 == arr[j]:
                    arr[i] , arr[j] = arr[j] ,arr[i]
                    ans+=1
                    
    return ans