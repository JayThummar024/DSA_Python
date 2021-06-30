dic = {}

arr = [2,7,11,15]

def twoSum(a , target):
    for i in range(len(a)):
        comp = target - arr[i]
        if a[i] in dic:
            return [dic[a[i]] , i]
        else:
            dic[comp] = i





        
