#attempt1:
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        startPosX,startPosY = -1,-1
        endPosX,endPosY = -1,-1
        totalNonObstacles = 0
        m,n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    startPosX,startPosY = x,y
                elif grid[x][y] == 2:
                    endPosX,endPosY = x,y
                elif grid[x][y] == 0:
                    totalNonObstacles += 1
        if (endPosX,endPosY) == (-1,-1) or (startPosX, startPosY) == (-1,-1):
            return 0
        ans = [0]
        def dfs(currentX, currentY, nonObstacles):
            if not(0<=currentX<m and 0<=currentY<n) or grid[currentX][currentY] == -1:
                return
            if currentX == endPosX and currentY == endPosY:
                ans[0] += (nonObstacles == totalNonObstacles+1)
                return
            prevVal = grid[currentX][currentY]
            grid[currentX][currentY] = -1
            for nextX,nextY in [(currentX+1,currentY),(currentX-1,currentY),(currentX,currentY+1),(currentX,currentY-1)]:
                dfs(nextX,nextY,nonObstacles+1)
            grid[currentX][currentY] = prevVal
        dfs(startPosX,startPosY,0)
        return ans[0]
            
            
