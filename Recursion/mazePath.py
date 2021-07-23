#given a n*m grid starting position is 0,0 AND we have to reach last cell...print all possible paths and count of all paths   

totalPaths = 0
def mazePath(i , j, osf , n , m ):  
    if i == n-1 and j == m-1:
        global totalPaths 
        totalPaths+=1
        print(osf)
        return

    if i >= n  or j >= m:
        return

    mazePath(i+1, j, osf+"D" , n ,m )
    mazePath(i, j+1, osf+"R" , n ,m)

    return totalPaths


print(mazePath(0,0,"", 3, 3))