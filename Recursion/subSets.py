def subSets(arr , i , ans=[] , gans = []):
    if len(arr)==i:
        if ans not in gans:
            gans.append(ans)
        return 

    subSets(arr, i+1 , ans+[arr[i]], gans)
    subSets(arr, i+1 , ans, gans)

    return gans


print(subSets([1,2,3] , 0))