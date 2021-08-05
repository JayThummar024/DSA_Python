mat = [
        [-5,-3,-2,-4],
        [-1,-4,-8,-3],
        [-6,-7,-2,-1],
        [-4,-3,-10,-12]
    ]
r=4
c=4


def Kadane(temp):
    gs = temp[0]
    cs = 0
    max_ele = max(temp)

    for i in range(len(temp)):
        cs = cs + temp[i]
        cs = max(cs ,0)
        gs = max(cs,gs)
        max_ele = max(max_ele , temp[i])

    if gs == 0:
        gs = max_ele

    return gs


def maxSumRect(arr , r , c):
    maxSum = arr[0][0]
    goArr = [0] * r
    for i in range(0 , c):
        for j in range(i , c):
            for k in range(r):
                goArr[k] += arr[k][j] 
            
            currSum = Kadane(goArr)
            maxSum = max(maxSum , currSum)

        goArr = [0]*r
    return maxSum

print(maxSumRect(mat, 4, 4))