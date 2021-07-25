count = 0
def isItSafe(grid ,visited , i , j , n):
    return i>=0 and j >=0 and i<n and j<n and visited[i][j] == False

def printGrid(grid):
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            print(grid[i][j] , end="   ")
        print()

def knightTour(grid , visited , i , j, n, cnt):
    global count
    if cnt == n*n - 1:
        grid[i][j] = cnt
        count += 1
        printGrid(grid)
        print()
        return
  

    row = [-2,-2,-1,-1,2,2,1,1]
    col = [1,-1,2,-2,1,-1,2,-2]
    grid[i][j] = cnt
    visited[i][j] = True
    for k in range(8):
        if isItSafe(grid ,visited , i + row[k] , j+col[k] , n):
            knightTour(grid , visited , i + row[k] , j+col[k] , n, cnt+1)
    grid[i][j] -= 1
    visited[i][j] = False

n=5
grid = [[0]*n for i in range(n)]
visited = [[False]*n for i in range(n)]
print(grid)
knightTour(grid, visited, 0, 0, n, 0)
print(count)