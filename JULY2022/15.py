#atttempt1:
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        allvisited = set()
        row_len = len(grid)
        col_len = len(grid[0])
        
        def dfs(row,col,visited):
            if not(0<=row<row_len) or not(0<=col<col_len) or not(grid[row][col]):
                return 0
            visited.add((row,col))
            for row_add,col_add in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (row_add+row,col_add+col) not in visited:
                    dfs(row_add+row,col_add+col,visited)
        
        maxans = 0
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] and (row,col) not in allvisited:
                    visited = set()
                    dfs(row,col,visited)
                    maxans = max(maxans,len(visited))
                    allvisited = allvisited|visited
        
        return maxans
