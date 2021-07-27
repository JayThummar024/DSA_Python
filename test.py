class Solution:
    def isValid(self , i,j,visited,n):
        return i>=0 and i<n and j>=0 and j<n and visited[i][j]==False
    
    def helper(self,i,j,grid,visited,n, osf,ans):
        if i==n-1 and j==n-1:
            ans.append(osf)
            return ans
    
        if not self.isValid(i, j, visited, n):
            return ans
    
        visited[i][j] =True
    
        if i+1 < n and grid[i+1][j] == 1:
            self.helper(i+1,j,grid,visited,n,osf+"D",ans)
    
        if j+1 < n and grid[i][j+1] == 1:
            self.helper(i,j+1,grid,visited,n,osf+"R",ans)
    
        if i-1 >= 0 and grid[i-1][j]==1:
            self.helper(i-1,j,grid,visited,n,osf+"U",ans)
    
        if j-1 >=0 and grid[i][j-1]==1:
            self.helper(i, j, grid, visited, n,osf+"L",ans)
    
        visited[i][j] = False
        return ans
    
    
    
    def findPath(self, m, n):
        # code here
        visited = [[False]*n for i in range(n)]
        ans = self.helper(0,0,m,visited,n,"",[])
        return ans



sol = Solution()
n=5
m = [[1]*5 for i in range(5)]
print(sol.findPath(m, n))