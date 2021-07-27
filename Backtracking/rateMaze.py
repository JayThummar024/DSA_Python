totalPaths = 0
ans = []

def isValid(i,j,visited,n):
    return i>=0 and i<n and j>=0 and j<n and visited[i][j]==False 

def helper(i,j,grid,visited,n, osf):
    global totalPaths
    global ans
    if i==n-1 and j==n-1:
        ans.append(osf)
        totalPaths+=1
        return

    if not isValid(i, j, visited, n):
        return

    visited[i][j] =True

    if i+1 < n and grid[i+1][j] == 1:
        helper(i+1,j,grid,visited,n,osf+"D")

    if j+1 < n and grid[i][j+1] == 1:
        helper(i,j+1,grid,visited,n,osf+"R")

    if i-1 >= 0 and grid[i-1][j]==1:
        helper(i-1,j,grid,visited,n,osf+"U")

    if j-1 >=0 and grid[i][j-1]==1:
        helper(i, j, grid, visited, n,osf+"L")

    visited[i][j] = False
    return
        
def rateMaze(i ,j,grid):
    n = len(grid)
    visited = [[False]*5 for i in range(5)]
    helper(0,0,grid,visited,n,"")
    return


grid = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
print(rateMaze(0, 0, grid))
print(ans)

