obs = [[0,0,0],[0,1,0],[0,0,0]]

count =0

def paths(i , j ,m , n , obs):
    global count
    if (i==m-1 and j==n-1):
        count+=1
        return
    
    if i > m-1 or j > n-1:
        return
    
    if i<m-1: 
        if not obs[i+1][j]==1:
            paths(i+1,j,m,n,obs)
    if j<n-1:
        if not obs[i][j+1]==1:
            paths(i,j+1,m,m,obs)

    return

paths(0,0,3,3,obs)
print(count)
