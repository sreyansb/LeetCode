#attempt4: Doesn't work
"""
class Solution:
    def uniquePathsIII(self, grid):
        no0=0
        start=()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                no0+=1 if grid[i][j]==0 else 0
                if not(start):
                    start=(i,j) if grid[i][j]==1 else ()
        if not(start):
            return 0 
        
        ans=[0]
        def dfs(i,j,count):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==-1:
                return
            #print(count==no0,count==no0+1,grid[i][j])
            if grid[i][j]==2:
                print(count)
                if count==no0+1:
                    ans[0]+=1
                    return
            grid[i][j]=-1
            dfs(i-1,j,count+1)
            dfs(i+1,j,count+1)
            dfs(i,j+1,count+1)
            dfs(i,j-1,count+1)
            grid[i][j]=0
        dfs(start[0],start[1],0)
        return(ans[0])
obj=Solution()
print(obj.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
"""
#attempt 3: 30% and 75%
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        no0=0
        start=()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                no0+=1 if grid[i][j]==0 else 0
                if not(start):
                    start=(i,j) if grid[i][j]==1 else ()
        if not(start):
            return 0 
        
        ans=[0]
        def dfs(i,j,visited):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i,j) in visited or grid[i][j]==-1:
                return
            if grid[i][j]==2:
                if len((visited))==no0+1:
                    ans[0]+=1
                    return
            visited.add((i,j))
            dfs(i-1,j,visited)
            dfs(i+1,j,visited)
            dfs(i,j+1,visited)
            dfs(i,j-1,visited)
            visited.remove((i,j))
        dfs(start[0],start[1],set())
        return(ans[0])
"""
#attempt2: 15% and 99% no hashing in the set.
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        no0=0
        start=()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                no0+=1 if grid[i][j]==0 else 0
                if not(start):
                    start=(i,j) if grid[i][j]==1 else ()
        if not(start):
            return 0 
        
        ans=[0]
        def dfs(i,j,visited):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i,j) in visited or grid[i][j]==-1:
                return
            if grid[i][j]==2:
                if len((visited))==no0+1:
                    ans[0]+=1
                    return
            visited.add((i,j))
            dfs(i-1,j,visited)
            dfs(i+1,j,visited)
            dfs(i,j+1,visited)
            dfs(i,j-1,visited)
            visited.remove((i,j))
        dfs(start[0],start[1],set())
        return(len(ans))
"""
#attempt1: 20% and 70%
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        no0=0
        start=()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                no0+=1 if grid[i][j]==0 else 0
                if not(start):
                    start=(i,j) if grid[i][j]==1 else ()
        if not(start):
            return 0 
        
        ans=set()
        def dfs(i,j,visited):
            #print(i,j)
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i,j) in visited or grid[i][j]==-1:
                return
            if grid[i][j]==2:
                #print(visited)
                if len(set(visited))==no0+1:
                    ans.add(tuple(visited+[(i,j)]))
                    return
            visited.append((i,j))
            dfs(i-1,j,visited)
            dfs(i+1,j,visited)
            dfs(i,j+1,visited)
            dfs(i,j-1,visited)
            visited.pop()
        dfs(start[0],start[1],[])
        return(len(ans))
"""       
            
        
        
