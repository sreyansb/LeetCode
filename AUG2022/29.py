#attempt1:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def findIsland(curRow,curCol):
            allVisited.add((curRow,curCol))
            for nextRow,nextCol in [(curRow+1,curCol),(curRow-1,curCol),(curRow,curCol+1),(curRow,curCol-1)]:
                if not(0<=nextRow<m and 0<=nextCol<n) or (nextRow,nextCol) in allVisited or grid[nextRow][nextCol] == "0":
                    continue
                findIsland(nextRow,nextCol)
            return
        allVisited = set()
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row,col) not in allVisited:
                    findIsland(row,col)
                    ans += 1
        return ans
                    
                
        
                
            
        
