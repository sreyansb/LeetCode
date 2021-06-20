#attempt4:AC
from heapq import heappush,heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        heap=[]
        t=0
        heappush(heap,(grid[0][0],(0,0)))
        finaltuple=(n-1,n-1)
        visited={(0,0)}
        while(heap[0][1]!=finaltuple):
            
            if heap[0][0]<=t:
                time,loc=heappop(heap)
                row,col=loc
                if row>0 and (row-1,col) not in visited:
                    visited.add((row-1,col))
                    heappush(heap,(max(time,grid[row-1][col]),(row-1,col)))
                if row<n-1 and (row+1,col) not in visited:
                    visited.add((row+1,col))
                    heappush(heap,(max(time,grid[row+1][col]),(row+1,col)))
                if col>0 and (row,col-1) not in visited:
                    visited.add((row,col-1))
                    heappush(heap,(max(time,grid[row][col-1]),(row,col-1)))
                if col<n-1 and (row,col+1) not in visited:
                    visited.add((row,col+1))
                    heappush(heap,(max(time,grid[row][col+1]),(row,col+1)))
            else:
                t+=1
                
        return heap[0][0]
                

#attempt3:WA because I forgot to take into consideration that starting point can have cost>0
'''
from heapq import heappush,heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        heap=[]
        t=0
        heappush(heap,(0,(0,0)))
        finaltuple=(n-1,n-1)
        visited={(0,0)}
        while(heap[0][1]!=finaltuple):
            
            if heap[0][0]<=t:
                time,loc=heappop(heap)
                row,col=loc
                if row>0 and (row-1,col) not in visited:
                    visited.add((row-1,col))
                    heappush(heap,(max(time,grid[row-1][col]),(row-1,col)))
                if row<n-1 and (row+1,col) not in visited:
                    visited.add((row+1,col))
                    heappush(heap,(max(time,grid[row+1][col]),(row+1,col)))
                if col>0 and (row,col-1) not in visited:
                    visited.add((row,col-1))
                    heappush(heap,(max(time,grid[row][col-1]),(row,col-1)))
                if col<n-1 and (row,col+1) not in visited:
                    visited.add((row,col+1))
                    heappush(heap,(max(time,grid[row][col+1]),(row,col+1)))
            else:
                t+=1
                
        return heap[0][0]
'''

#Attempt2: TLE 40/41 MAde the changes wherein if you are visiting the new node with lesser entry time you update that time in visited
#visited is a dictionary which holds entry time into the cell
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visited={}
        def swim(row,col,time):
            if not(0<=row<n and 0<=col<n):
                return float('inf')
            if row==n-1 and col==n-1:
                return time
            if (row,col) in visited and visited[(row,col)]<=time:
                return float('inf')
            visited[(row,col)]=time
            ans=float('inf')
            if row>0:
                maxie=max(grid[row-1][col],grid[row][col])
                if maxie<=time:
                    ans=min(ans,swim(row-1,col,time))
                else:
                    ans=min(ans,swim(row-1,col,maxie))
            if row<n-1:
                maxie=max(grid[row+1][col],grid[row][col])
                if maxie<=time:
                    ans=min(ans,swim(row+1,col,time))
                else:
                    ans=min(ans,swim(row+1,col,maxie))
            if col>0:
                maxie=max(grid[row][col-1],grid[row][col])
                if maxie<=time:
                    ans=min(ans,swim(row,col-1,time))
                else:
                    ans=min(ans,swim(row,col-1,maxie))
            if col<n-1:
                maxie=max(grid[row][col+1],grid[row][col])
                if maxie<=time:
                    ans=min(ans,swim(row,col+1,time))
                else:
                    ans=min(ans,swim(row,col+1,maxie))
            return ans
        return swim(0,0,0)
'''

#attempt1:WA because you can enter a cell with lesser timings than the time it was entered before
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visited=set()
        def swim(row,col,time):
            if not(0<=row<n and 0<=col<n):
                return float('inf')
            if row==n-1 and col==n-1:
                return time
            if (row,col) in visited:#to prevent recursion depth reached
                return float('inf')
            visited.add((row,col))
            ans=float('inf')
            if row>0:
                maxie=max(grid[row-1][col],grid[row][col])
                if maxie<=time:
                    ans=min(ans,swim(row-1,col,time))
                else:
                    ans=min(ans,swim(row-1,col,maxie))
            if row<n-1:
                maxie=max(grid[row+1][col],grid[row][col])
                if maxie<=time:
                    ans=min(ans,swim(row+1,col,time))
                else:
                    ans=min(ans,swim(row+1,col,maxie))
            if col>0:
                maxie=max(grid[row][col-1],grid[row][col])
                if maxie<=time:
                    ans=min(ans,swim(row,col-1,time))
                else:
                    ans=min(ans,swim(row,col-1,maxie))
            if col<n-1:
                maxie=max(grid[row][col+1],grid[row][col])
                if maxie<=time:
                    ans=min(ans,swim(row,col+1,time))
                else:
                    ans=min(ans,swim(row,col+1,maxie))
            return ans
        return swim(0,0,0)
                
'''