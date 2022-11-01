#attempt1: TOOK HINT
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        if n == 1:
            return [-1]
        ans = [-1]*n
        @lru_cache(None)
        def dfs(curRow,curCol):
            #print(curRow,curCol)
            if curRow == m:
                return curCol
            if grid[curRow][curCol] == 1:
                if curCol+1 == n or grid[curRow][curCol+1] == -1:
                    return -1
                return dfs(curRow+1,curCol+1)
            else:
                if curCol == 0 or grid[curRow][curCol-1] == 1:
                    return -1
                return dfs(curRow+1,curCol-1)
        for col in range(n):
            ans[col] = dfs(0,col)
        return ans
