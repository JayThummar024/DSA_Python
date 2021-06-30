def doIntersection(a,b):
    intersection=[]
    for i in range(len(a)):
        if a[i] in b:
            intersection.append(a[i])
    return intersection