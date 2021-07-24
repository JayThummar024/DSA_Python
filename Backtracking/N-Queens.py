cnt = 0

def LD(row , col , grid , n):
    i = row
    j = col
    while i>=0 and j>=0:
        if grid[i][j] == 1:
            return False
        i-=1
        j-=1

    return True

def UP(row , col , grid , n):
    i = row
    j = col
    while i>=0:
        if grid[i][j] == 1:
            return False
        i-=1

    return True

def RD(row , col , grid , n):
    i = row
    j = col
    while i>=0 and j<n:
        if grid[i][j] == 1:
            return False
        i-=1
        j+=1

    return True



def helper(row , grid , n):
    global cnt
    if row == n:
        cnt+=1
        printGrid(grid)
        print()
        return

    for col in range(n):
        if LD(row,col,grid,n) and UP(row,col,grid,n) and RD(row,col,grid,n):
            grid[row][col] = 1
            helper(row+1 , grid , n)
            grid[row][col] = 0  

def NQueens(n):
    grid = [[0]*n for i in range(n)]
    helper(0 , grid , n)

def printGrid(grid):
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                print("Q" , end=" ")
            else:
                print("." , end=" ")
        print()

NQueens(4)
print(cnt)