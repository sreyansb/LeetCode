#attempt5:
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dpt=[[-1 for i in range(m)]for j in range(n)]
        def components(r,c,compn,visited):
            dpt[r][c]=compn
            if r+1<n and grid[r+1][c] and dpt[r+1][c]==-1:
                visited[0]+=1
                components(r+1,c,compn,visited)
            if c+1<m and grid[r][1+c] and dpt[r][1+c]==-1:
                visited[0]+=1
                components(r,c+1,compn,visited)
            if r-1>-1 and grid[r-1][c] and dpt[r-1][c]==-1:
                visited[0]+=1
                components(r-1,c,compn,visited)
            if c-1>-1 and grid[r][c-1] and dpt[r][c-1]==-1:
                visited[0]+=1
                components(r,c-1,compn,visited)
        comp=0
        ans=1
        compsize={}
        for r in range(n):
            for c in range(m):
                if grid[r][c] and dpt[r][c]==-1:
                    visited=[1]
                    components(r,c,comp,visited)
                    compsize[comp]=visited[0]
                    ans=max(compsize[comp],ans)
                    comp+=1
        #print(compsize)
        compsize[-1]=0
        for r in range(n):
            for c in range(m):
                if grid[r][c]==0:
                    final=set()
                    for a,b in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                        if (0<=a<n and 0<=b<m):
                            final.add(dpt[a][b])
                    f=1+sum([compsize[i] for i in final])
                    ans=max(ans,f)
        return ans

#attempt4: AC. final is a set which describes the nummber of distinct components
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dpt=[[-1 for i in range(m)]for j in range(n)]
        def components(r,c,compn,visited):
            dpt[r][c]=compn
            if r+1<n and grid[r+1][c] and dpt[r+1][c]==-1:
                visited[0]+=1
                components(r+1,c,compn,visited)
            if c+1<m and grid[r][1+c] and dpt[r][1+c]==-1:
                visited[0]+=1
                components(r,c+1,compn,visited)
            if r-1>-1 and grid[r-1][c] and dpt[r-1][c]==-1:
                visited[0]+=1
                components(r-1,c,compn,visited)
            if c-1>-1 and grid[r][c-1] and dpt[r][c-1]==-1:
                visited[0]+=1
                components(r,c-1,compn,visited)
        comp=0
        ans=1
        compsize={}
        for r in range(n):
            for c in range(m):
                if grid[r][c] and dpt[r][c]==-1:
                    visited=[1]
                    components(r,c,comp,visited)
                    compsize[comp]=visited[0]
                    ans=max(compsize[comp],ans)
                    comp+=1
        #print(compsize)
        compsize[-1]=0
        for r in range(n):
            for c in range(m):
                if grid[r][c]==0:
                    final=set()
                    for p1,p2 in [((r-1,c),(r,c-1)),((r-1,c),(r,c+1)),((r-1,c),(r+1,c)),((r+1,c),(r,c-1)),((r+1,c),(r,c+1)),((r,c-1),(r,c+1))]:
                        if (0<=p1[0]<n and 0<=p1[1]<m) and dpt[p1[0]][p1[1]]!=-1:
                                final.add(dpt[p1[0]][p1[1]])
                        if (0<=p2[0]<n and 0<=p2[1]<m) and dpt[p2[0]][p2[1]]!=-1:
                                final.add(dpt[p2[0]][p2[1]])
                    f=1+sum([compsize[i] for i in final])
                    ans=max(ans,f)
        return ans
'''

#attempt3: WA as I just considered that 0 is a bridge between atmost 2 components
'''
from functools import lru_cache
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dpt=[[-1 for i in range(m)]for j in range(n)]
        def components(r,c,compn,visited):
            dpt[r][c]=compn
            if r+1<n and grid[r+1][c] and dpt[r+1][c]==-1:
                visited[0]+=1
                components(r+1,c,compn,visited)
            if c+1<m and grid[r][1+c] and dpt[r][1+c]==-1:
                visited[0]+=1
                components(r,c+1,compn,visited)
            if r-1>-1 and grid[r-1][c] and dpt[r-1][c]==-1:
                visited[0]+=1
                components(r-1,c,compn,visited)
            if c-1>-1 and grid[r][c-1] and dpt[r][c-1]==-1:
                visited[0]+=1
                components(r,c-1,compn,visited)
        comp=0
        ans=1
        compsize={}
        for r in range(n):
            for c in range(m):
                if grid[r][c] and dpt[r][c]==-1:
                    visited=[1]
                    components(r,c,comp,visited)
                    compsize[comp]=visited[0]
                    ans=max(compsize[comp],ans)
                    comp+=1
        #print(dpt,compsize)
        compsize[-1]=0
        for r in range(n):
            for c in range(m):
                if grid[r][c]==0:
                    for p1,p2 in [((r-1,c),(r,c-1)),((r-1,c),(r,c+1)),((r-1,c),(r+1,c)),((r+1,c),(r,c-1)),((r+1,c),(r,c+1)),((r,c-1),(r,c+1))]:
                        if (0<=p1[0]<n and 0<=p1[1]<m) and (0<=p2[0]<n and 0<=p2[1]<m):
                            if dpt[p1[0]][p1[1]]!=dpt[p2[0]][p2[1]]:
                                ans=max(ans,compsize[dpt[p1[0]][p1[1]]]+1+compsize[dpt[p2[0]][p2[1]]])
                        else:
                            if (0<=p1[0]<n and 0<=p1[1]<m) and dpt[p1[0]][p1[1]]!=-1:
                                ans=max(ans,compsize[dpt[p1[0]][p1[1]]]+1)
                            if (0<=p2[0]<n and 0<=p2[1]<m) and dpt[p2[0]][p2[1]]!=-1:
                                ans=max(ans,1+compsize[dpt[p2[0]][p2[1]]])
        return ans
'''

#attempt2:
#IDEA: precalculate connected components only for 1s and put into a dpt table
#FOR each component keep the size of the connected component
#THEN for each 0 (consider that as a bridge between 1-4 components) and maintain that
'''
from functools import lru_cache
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dpt=[[-1 for i in range(m)]for j in range(n)]
        def components(r,c,compn,visited):
            dpt[r][c]=compn
            if r+1<n and grid[r+1][c] and dpt[r+1][c]==-1:
                visited[0]+=1
                components(r+1,c,compn,visited)
            if c+1<m and grid[r][1+c] and dpt[r][1+c]==-1:
                visited[0]+=1
                components(r,c+1,compn,visited)
            if r-1>-1 and grid[r-1][c] and dpt[r-1][c]==-1:
                visited[0]+=1
                components(r-1,c,compn,visited)
            if c-1>-1 and grid[r][c-1] and dpt[r][c-1]==-1:
                visited[0]+=1
                components(r,c-1,compn,visited)
        comp=0
        ans=1
        compsize={}
        for r in range(n):
            for c in range(m):
                if grid[r][c] and dpt[r][c]==-1:
                    visited=[1]
                    components(r,c,comp,visited)
                    compsize[comp]=visited[0]
                    ans=max(compsize[comp],ans)
                    comp+=1
        #print(dpt,compsize)
        for r in range(n):
            for c in range(m):
                if grid[r][c]==0:
                    for p1,p2 in [((r-1,c),(r,c-1)),((r-1,c),(r,c+1)),((r-1,c),(r+1,c)),((r+1,c),(r,c-1)),((r+1,c),(r,c+1)),((r,c-1),(r,c+1))]:
                        if (0<=p1[0]<n and 0<=p1[1]<m) and (0<=p2[0]<n and 0<=p2[1]<m):
                            if dpt[p1[0]][p1[1]]!=dpt[p2[0]][p2[1]]:
                                ans=max(ans,compsize[dpt[p1[0]][p1[1]]]+1+compsize[dpt[p2[0]][p2[1]]])
                        else:
                            if (0<=p1[0]<n and 0<=p1[1]<m) and dpt[p1[0]][p1[1]]!=-1:
                                ans=max(ans,compsize[dpt[p1[0]][p1[1]]]+1)
                            if (0<=p2[0]<n and 0<=p2[1]<m) and dpt[p2[0]][p2[1]]!=-1:
                                ans=max(ans,1+compsize[dpt[p2[0]][p2[1]]])
        return ans
'''

#attempt1: I dont know what I am doing here
'''
from functools import lru_cache
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ans=1
        n=len(grid)
        m=len(grid[0])
        visited=set()
        @lru_cache(None)
        def component(row,col,haszero):
            if (row,col) in visited:
                return 0
            visited.add((row,col))
            anshere=1
            if haszero:
                if row+1<n and grid[row+1][col]:
                    anshere+=component(row+1,col,haszero)
                if row-1>-1 and grid[row-1][col]:
                    anshere+=component(row-1,col,haszero)
                if col+1<m and grid[row][col+1]:
                    anshere+=component(row,col+1,haszero)
                    #anshere+=dpt[(row,col+1,haszero)]
                if col-1>-1 and grid[row][col-1]:
                    anshere+=component(row,col-1,haszero)
                    #anshere+=dpt[(row,col-1,haszero)]
            else:
                zeroes=set()
                allowed=set()
                if row+1<n:
                    allowed.add((row+1,col))
                    if grid[row+1][col]==0:
                        zeroes.add((row+1,col))
                if col+1<m:
                    allowed.add((row,col+1))
                    if grid[row][col+1]==0:
                        zeroes.add((row,col+1))
                if row-1>-1:
                    allowed.add((row-1,col))
                    if grid[row-1][col]==0:
                        zeroes.add((row-1,col))
                if col-1>-1:
                    allowed.add((row,col-1))
                    if grid[row][col-1]==0:
                        zeroes.add((row,col-1))
                curans=0
                for r,c in zeroes:
                    hereans=component(r,c,1)
                    curans=max(curans,hereans)
                for r,c in allowed-zeroes:
                    hereans=0
                    if grid[r][c]:
                        hereans=component(r,c,0)
                    curans+=hereans
                anshere+=curans
            return anshere
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    visited=set()
                    ans=max(ans,component(i,j,0))
        return ans        
'''