result = []

def util(arr, nT ,osf):
    global result
    if nT == 0:
        x = osf.copy()
        x.sort()
        if x not in result:
            result.append(x)
        return

    if nT < 0:
        return

    for i in range(len(arr)):
        newTar = nT - arr[i]
        osf = osf + [arr[i]]
        newArr = arr[i+1:]
        util(newArr,newTar ,osf)
        osf.pop()



# approach 2
res = []
arr= [2,1,2]
space = sorted(arr)
target = 3
        
def dfs(space,track,remain):
    global res
    if remain == 0:
        res.append(track)
    for i in range(len(space)):
        if space[i] > remain:
            break
        if i > 0 and space[i] == space[i-1]:
            continue
        dfs(space[i+1:],track+[space[i]],remain-space[i])

dfs(space,[],target)


print(res)

