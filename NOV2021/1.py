#attempt1: 260ms

class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        m,n = len(grid),len(grid[0])
        allvisited = set()
        
        def getconnectedcomponents(crow,ccol,visited):
            visited.add((crow,ccol))
            for i,j in [(crow-1,ccol),(crow+1,ccol),(crow,ccol-1),(crow,ccol+1)]:
                if (0<i<m-1) and (0<j<n-1) and grid[i][j] == "O" and (i,j) not in visited:
                    getconnectedcomponents(i,j,visited)
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == "O" and (i,j) not in allvisited:
                    visited = set()
                    getconnectedcomponents(i,j,visited)
                    flag = 1
                    for r,c in sorted(visited, key = lambda x : (x[0],x[1])):
                        if not(((r-1,c) in visited or grid[r-1][c] == 'X') and ((r+1,c) in visited or grid[r+1][c] == 'X') and ((r,c-1) in visited or grid[r][c-1] == 'X') and ((r,c+1) in visited or grid[r][c+1] == 'X')):
                            flag = 0
                            break
                    if flag:
                        for r,c in visited:
                            grid[r][c] = 'X'
                
                    allvisited = allvisited|visited