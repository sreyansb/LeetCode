#attempt2:
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if grid[0][0]:
            return 0
        grid[0][0]=1
        for i in range(1,n):
            grid[0][i]=not(grid[0][i]) and grid[0][i-1]
        for i in range(1,m):
            grid[i][0]=not(grid[i][0]) and grid[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]:
                    grid[i][j]=0
                else:
                    grid[i][j]=grid[i-1][j]+grid[i][j-1]
               
        return int(grid[m-1][n-1])

#attempt1:
'''
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        dp=[[-1 for i in range(n)]for j in range(m)]
        def check(r,c):
            if r>=m or c>=n or grid[r][c]:
                return 0
            if r==m-1 and c==n-1:
                return 1
            if dp[r][c]!=-1:
                return dp[r][c]
            dp[r][c]=check(r+1,c)+check(r,c+1)
            return dp[r][c]
        return check(0,0)
'''
