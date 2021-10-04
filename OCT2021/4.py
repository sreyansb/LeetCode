#attempt2:
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        ans=[0]
        m,n=len(grid),len(grid[0])
        def connectedcomp(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))
            numberconnectedto=0
            if c+1<n and grid[r][c+1]:
                numberconnectedto+=1
                connectedcomp(r,c+1)
            if r+1<m and grid[r+1][c]:
                numberconnectedto+=1
                connectedcomp(r+1,c)
            if r-1>=0 and grid[r-1][c]:
                numberconnectedto+=1
                connectedcomp(r-1,c)
            if c-1>=0 and grid[r][c-1]:
                numberconnectedto+=1
                connectedcomp(r,c-1)
            ans[0]+=4-numberconnectedto
        for i in range(m):
            if 1 in grid[i]:
                connectedcomp(i,grid[i].index(1))
                break
        return ans[0]

#attempt1:
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        ans=[0]
        m,n=len(grid),len(grid[0])
        def connectedcomp(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))
            numberconnectedto=0
            if c+1<n and grid[r][c+1]:
                numberconnectedto+=1
                connectedcomp(r,c+1)
            if r+1<m and grid[r+1][c]:
                numberconnectedto+=1
                connectedcomp(r+1,c)
            if r-1>=0 and grid[r-1][c]:
                numberconnectedto+=1
                connectedcomp(r-1,c)
            if c-1>=0 and grid[r][c-1]:
                numberconnectedto+=1
                connectedcomp(r,c-1)
            ans[0]+=4-numberconnectedto
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    connectedcomp(i,j)
        return ans[0]
'''