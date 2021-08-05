result = []

def util(arr, nT ,osf):
    global result
    if nT == 0:
        x = osf.copy()
        x.sort()
        if x not in result:
            result.append(osf.copy())
        return

    if nT < 0:
        return

   
    for i in range(len(arr)):
        newTar = nT - arr[i]
        osf = osf + [arr[i]]
        util(arr ,newTar ,osf)
        osf.pop()


arr= [3,12,9,15]
target = 15
util(arr,target,[])
print(result)

