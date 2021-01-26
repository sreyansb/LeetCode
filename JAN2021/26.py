#attempt2:
from heapq import heappush,heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        ind=float('inf')
        
        dp=[[ind for i in range(cols)] for i in range(rows)]
        dp[0][0]=0
        empty=[]
        heappush(empty,(0,0,0))
        
        while(empty):
            #print(empty)
            maxie,row,col=heappop(empty)
            if row==rows-1 and col==cols-1:
                return maxie
            #dp[row][col]=maxie
            #print(row,col,maxie)
            for xd in [-1,1]:
                x,y=row+xd,col+xd
                if x>=0 and x<rows:
                    lowdiff=max(maxie,abs(heights[row][col]-heights[x][col]))
                    if dp[x][col]>lowdiff:
                        dp[x][col]=lowdiff
                        heappush(empty,(lowdiff,x,col))
                if y>=0 and y<cols:
                    lowdiff=max(maxie,abs(heights[row][col]-heights[row][y]))
                    if dp[row][y]>lowdiff:
                        dp[row][y]=lowdiff
                        heappush(empty,(lowdiff,row,y))

#attempt3: TLE 5/75
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        ind=float('inf')
        dp=[[-1 for i in range(cols)] for i in range(rows)]
        def dfs(row,col,maxie=0):
            if row==rows-1 and col==cols-1:
                return maxie
            copy=heights[row][col]
            heights[row][col]=ind
            #print(row,col,maxie)
            maxdiff=ind
            newpoints=[(row+1,col),(row,col+1),(row-1,col),(row,col-1)]
            newpoints=[i for i in newpoints if i[0]>-1 and i[0]<rows and i[1]>-1 and i[1]<cols]
            newpoints.sort(key=lambda x:max(maxie,abs(heights[x[0]][x[1]]-copy)))
            for points in newpoints:
                x,y=points
                lowdiff=max(maxie,abs(copy-heights[x][y]))
                if lowdiff==ind:
                    continue
                maxdiff=min(maxdiff,dfs(x,y,lowdiff))                          
            dp[row][col]=maxdiff
            heights[row][col]=copy
            return maxdiff
        return dfs(0,0)
'''

#attempt1:TLE 5/75
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        ind=float('inf')
        dp=[[-1 for i in range(cols)] for i in range(rows)]
        def dfs(row,col,maxie=0):
            if row==rows-1 and col==cols-1:
                return maxie
            if row>=rows or col>=cols or row<0 or col<0:
                return ind
            dp[row][col]=0
            #print(row,col,maxie)
            maxdiff=ind
            for xd in [-1,1]:
                    try:
                        lowdiff=abs(heights[row][col]-heights[row+xd][col])
                        if dp[row+xd][col]==-1 or dp[row+xd][col]>lowdiff:
                            x,y=row+xd,col
                            maxdiff=min(maxdiff,dfs(x,y,max(maxie,lowdiff)))
                    except:
                        pass
                    try:
                        lowdiff=abs(heights[row][col]-heights[row][col+xd])
                        if dp[row][col+xd]==-1 or dp[row][col+xd]>lowdiff:
                            x,y=row,col+xd
                            maxdiff=min(maxdiff,dfs(x,y,max(maxie,lowdiff)))
                    except:
                        pass
            dp[row][col]=maxdiff
            return maxdiff
        return dfs(0,0)
            
        
'''
