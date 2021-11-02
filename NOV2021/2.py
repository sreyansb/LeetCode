#attempt2: 92ms
'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        sr,sc,empty = -1,-1,0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    sr = i
                    sc = j
                elif grid[i][j]==0:
                    empty += 1
        ans = [0]
        def dfs(cur,cuc,count,visited):
            if grid[cur][cuc] == 2 and count == empty+1:
                ans[0] += 1
                return
            for i,j in [(cur-1,cuc),(cur+1,cuc),(cur,cuc+1),(cur,cuc-1)]:
                if (0<=i<m and 0<=j<n) and grid[i][j]!=-1 and (i,j) not in visited :
                    dfs(i,j,count+1,visited|{(cur,cuc)})
        dfs(sr,sc,0,set())
        return ans[0]
'''

#attempt1: 80ms
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        sr,sc,empty = -1,-1,0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    sr = i
                    sc = j
                elif grid[i][j]==0:
                    empty += 1
        ans = [0]
        def dfs(cur,cuc,visited):
            if grid[cur][cuc] == 2 and len(visited) == empty+1:
                ans[0] += 1
                return
            for i,j in [(cur-1,cuc),(cur+1,cuc),(cur,cuc+1),(cur,cuc-1)]:
                if (0<=i<m and 0<=j<n) and grid[i][j]!=-1 and (i,j) not in visited :
                    dfs(i,j,visited|{(cur,cuc)})
        dfs(sr,sc,set())
        return ans[0] 
            
                