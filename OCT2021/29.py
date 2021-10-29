#attempt2: AC
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def checkallrotten(grid):
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        return False
            return True
        
        def makepossiblerotten(grid):
            newgrid = [[0 for i in range(n)]for j in range(m)]
            
            for i in range(m):
                for j in range(n):
                    newgrid[i][j] = grid[i][j]
                    
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        if i-1 > -1 and grid[i-1][j] == 1:
                            newgrid[i-1][j] = 2
                        if j-1 > -1 and grid[i][j-1] == 1:
                            newgrid[i][j-1] = 2
                        if i+1 < m and grid[i+1][j] == 1:
                            newgrid[i+1][j] = 2
                        if j+1 < n and grid[i][j+1] == 1:
                            newgrid[i][j+1] = 2
            
            return newgrid
        count = 0
        while(True):
            if checkallrotten(grid):
                return count
            count += 1
            newgrid  = makepossiblerotten(grid)
            if newgrid == grid:
                return -1
            grid = newgrid

#attempt1: Slight oversight in the j condition of makepossiblerotten
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def checkallrotten(grid):
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        return False
            return True
        
        def makepossiblerotten(grid):
            newgrid = [[0 for i in range(n)]for j in range(m)]
            
            for i in range(m):
                for j in range(n):
                    newgrid[i][j] = grid[i][j]
                    
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        if i-1 > -1 and grid[i-1][j] == 1:
                            newgrid[i-1][j] = 2
                        if j-1 > 0 and grid[i][j-1] == 1:
                            newgrid[i][j-1] = 2
                        if i+1 < m and grid[i+1][j] == 1:
                            newgrid[i+1][j] = 2
                        if j+1 < n and grid[i][j+1] == 1:
                            newgrid[i][j+1] = 2
            
            return newgrid
        count = 0
        while(True):
            if checkallrotten(grid):
                return count
            count += 1
            newgrid  = makepossiblerotten(grid)
            if newgrid == grid:
                return -1
            grid = newgrid
'''