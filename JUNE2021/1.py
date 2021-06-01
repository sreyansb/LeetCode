#attempt1: DONT USE MAX in the recursive part
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        m=len(grid)
        n=len(grid[0])
        def connectedcomponents(x,y):
            if x<0 or y<0 or x>m-1 or y>n-1 or grid[x][y]==0 or (x,y) in visited:
                return 0
            visited.add((x,y))
            ans=0
            for xa,yb in [(-1,0),(1,0),(0,-1),(0,1)]:
                ans+=connectedcomponents(x+xa,y+yb)
            return ans+1
        maxi=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in visited:
                    maxi=max(maxi,connectedcomponents(i,j))
                    #print(i,j,maxi)
        return maxi
                    
                
        