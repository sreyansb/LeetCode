#attempt1:
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if not(m):
            return 0
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]:
            return 0
        @lru_cache(None)
        def movement(row,col):
            if row == m-1 and col == n-1:
                return 1
            if not(0<=row<m) or not(0<=col<n) or obstacleGrid[row][col] == 1:
                return 0
            ans = 0
            for x,y in [(row+1,col),(row,col+1)]:
                ans += movement(x,y)
            return ans
        return movement(0,0)
            
