####################### write a programme to reverse an array from start to end #########################

def reverseArr(arr , start ,end):
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start+=1
        end-=1
    return arr



def revArr(arr):
    return arr[::-1]


########################### Find the minimum and maximum no. in an array ####################################

def minmax(arr):
    min = 0
    max = 0
    if len(arr) == 1:
        min = arr[0]
        max = arr[0]
    if len(arr) == 2 and arr[0] > arr[1]:
        min = arr[1]
        max = arr[0]
    if len(arr) == 2 and arr[0] < arr[1]:
        min = arr[0]
        max = arr[1]
    if len(arr) > 2:
        min = arr[0]
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
            if arr[i] > max:
                max = arr[i]
    return {"min" : min , "max":max}



############################### sort array with 0,1,2 without any sorting algo####################

def sort012(arr,n):
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for i in range(n):
            if arr[i] == 0:
                cnt0+=1
             
            elif arr[i] == 1:
                cnt1+=1
                 
            elif arr[i] == 2:
                cnt2+=1
     
    # Update the array
        i = 0
     
    # Store all the 0s in the beginning
        while (cnt0 > 0):
            arr[i] = 0
            i+=1
            cnt0-=1
     
    # Then all the 1s
        while (cnt1 > 0):
            arr[i] = 1
            i+=1
            cnt1-=1
     
    # Finally all the 2s
        while (cnt2 > 0):
            arr[i] = 2
            i+=1
            cnt2-=1
        # code here
        return arr

############################Move all negative elements to one side of an array###################

def negSort(a):
    for i in range(len(a)):
        if a[i] > 0:
            a.append(a[i])
            a.remove(a[i])
    return a


############################ Find union and intersection of two sorted array ########################

def doUnion(a,b):
    #code here
    U = []
    for i in range(len(a)):
        if a[i] in U:
            continue
        else:
            U.append(a[i])
    for i in range(len(b)):
        if b[i] in U:
            continue
        else:
            U.append(b[i])
    return(U)

def doIntersection(a,b):
    intersection=[]
    for i in range(len(a)):
        if a[i] in b:
            intersection.append(a[i])
    return intersection


####################################### Rotate an array by one position ############################

def rotate( arr, n):
    last = arr[-1]
    arr.pop()
    arr.insert(0,last)
    return arr


################################### how to find pair whose sum is equal to target ##############

def piarSum(arr , target):
    pairs = []
    for i in range(len(arr)):
        for k in range(i+1 , len(arr)):
            if arr[i]+arr[k]==target:
                pairs.extend([[arr[i],arr[k]]])
    return pairs

###################### How to fin a missing number from a list of integers from 1 to 10 ###############

def missing(arr):
    sum10 = 10*11/2
    sumArr = sum(arr)
    return sum10 - sumArr

###################### Find max product of two elements in given array ####################

def maxProd(arr):
    max = 1
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i]*arr[j] > max:
                max = arr[i]*arr[j]
    return max 

def mProd(arr):
    arr.sort()
    return arr[-1]*arr[-2]

print(mProd([0,1,2,5,2,8,9]))


############################# Minimise the maximum difference between heights [V.IMP] ###############################

def getMinDiff(arr, n, k):
        arr.sort()
        mxs=[]
        mns=[]
        for i in arr:
            mxs.append(i+k)
            mns.append(i-k)
        ans=arr[-1]-arr[0]
        for i in range(1,n):
            if(mns[i]>=0):
                ans=min(ans,max(mns[n-1],mxs[i-1])-min(mns[i],mxs[0]))
        return ans

# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output:
# 5
# Explanation:
# The array can be modified as 
# {3, 3, 6, 8}. The difference between 
# the largest and the smallest is 8-3 = 5.


############################  Find the min no of jumps to reach last element of an array ##################

def minJumps(a):
    if len(a) == 1:
        return 0
    if a[0] == 0:
        return -1
    mi = a[0]
    step = a[0]
    jump = 1
    for i in range(1,len(a)):
        if i == len(a):
            return jump
        mi = max(mi , i+a[i])
        step-=1
        if step == 0:
            jump+=1
            if i < mi:
                return -1
            step = mi - i
    return -1

#######################   










    