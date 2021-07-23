obs = [[0,0,0],[0,1,0],[0,0,0]]
count =0
def paths(i , j ,m , n , obs ):
    global count
    if (i==n-1 and j==n-1):
        return 1
    
    if i > m and j > n:
        return 0
    
    if i<m-1: 
        if obs[i+1][j] == 1:
            return 0
        else:
            count = count + paths(i+1,j,m,n,obs)
    if j<n-1:
        if obs[i][j+1]==1:
            return 0
        else:
            count = count + paths(i,j+1,m,m,obs)

    return count

print(paths(0,0,3,3,obs))
print(count)
