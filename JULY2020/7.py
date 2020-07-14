def calperimeter(grid,i,j,n,m):
    peri=4
    if i==0:
        if j==0:
            if i+1!=n:
                if grid[i+1][j]:
                    peri-=1
            if j+1!=m:
                if grid[i][j+1]:
                    peri-=1
        
        elif j==m-1:
            if j!=0:
                if grid[i][j-1]:
                    peri-=1
            if i!=n-1:
                if grid[i+1][j]:
                    peri-=1
        else:
            if i+1!=n:
                if grid[i+1][j]:
                    peri-=1
            if j+1!=m:
                if grid[i][j+1]:
                    peri-=1
            if j!=0:
                if grid[i][j-1]:
                    peri-=1
    
    elif i==n-1:
        if j==0:
            if i!=0:
                if grid[i-1][j]:
                    peri-=1
            if j+1!=m:
                if grid[i][j+1]:
                    peri-=1
        elif j==m-1:
            if j!=0:
                if grid[i][j-1]:
                    peri-=1
            if i!=0:
                if grid[i-1][j]:
                    peri-=1
        else:
            if i!=0 and grid[i-1][j]:
                peri-=1
            if j+1!=m and grid[i][j+1]:
                peri-=1
            if j!=0 and grid[i][j-1]:
                peri-=1
    
    else:
        if j==0:
            if i+1!=n and grid[i+1][j]:
                peri-=1
            if i!=0 and grid[i-1][j]:
                peri-=1
            if j+1!=m and grid[i][j+1]:
                peri-=1
        elif j==m-1:
            if j!=0 and grid[i][j-1]:
                peri-=1
            if i!=0 and grid[i-1][j]:
                peri-=1
            if i+1!=n and grid[i+1][j]:
                peri-=1
        else:
            if i!=0 and grid[i-1][j]:
                peri-=1
            if j+1!=m and grid[i][j+1]:
                peri-=1
            if j!=0 and grid[i][j-1]:
                peri-=1
            if i+1!=n and grid[i+1][j]:
                peri-=1
          
    return peri
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        n=len(grid)
        for i in range(n):
                for j in range(len(grid[i])):
                    if grid[i][j]:
                        perimeter+=calperimeter(grid,i,j,n,len(grid[i]))
        return perimeter
                    
        
