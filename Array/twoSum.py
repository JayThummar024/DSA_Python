def piarSum(arr , target):
    pairs = []
    for i in range(len(arr)):
        for k in range(i+1 , len(arr)):
            if arr[i]+arr[k]==target:
                pairs.extend([[arr[i],arr[k]]])
    return pairs