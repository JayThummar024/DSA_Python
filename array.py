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
        min = a[0]
        max = a[0]
    if len(arr) == 2 and a[0] > a[1]:
        min = a[1]
        max = a[0]
    if len(arr) == 2 and a[0] < a[1]:
        min = a[0]
        max = a[1]
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

############################Move all negative elements to one side o an array###################

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

######################
