#attempt3:
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        queue=deque([])
        queue.append((0,0,k,0))
        visited={(0,0,k)}
        ans=float('inf')
        while(queue):
            curr,curc,curk,curd=queue.popleft()
            if curr==m-1 and curc==n-1:
                ans=min(ans,curd)
                continue
            for nextr,nextc in [(curr-1,curc),(curr+1,curc),(curr,curc-1),(curr,curc+1)]:
                if (0<=nextr<m and 0<=nextc<n):
                    if grid[nextr][nextc]:
                        if curk==0:
                            pass
                        else:
                            if (nextr,nextc,curk-1) not in visited:
                                visited.add((nextr,nextc,curk-1))
                                queue.append((nextr,nextc,curk-1,curd+1))
                    else:
                        if (nextr,nextc,curk) not in visited:
                            visited.add((nextr,nextc,curk))
                            queue.append((nextr,nextc,curk,curd+1))
        return ans if ans!=float('inf') else -1

#attempt2: WA because BFS doesn't guarantee shortest path with k
#we need to have 'k' part in the queue and visited
'''
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        queue=deque([])
        queue.append((0,0,k,0))
        visited={(0,0)}
        while(queue):
            curr,curc,curk,curd=queue.popleft()
            if curr==m-1 and curc==n-1:
                return curd
            for nextr,nextc in [(curr-1,curc),(curr+1,curc),(curr,curc-1),(curr,curc+1)]:
                if (0<=nextr<m and 0<=nextc<n) and (nextr,nextc) not in visited:
                    if grid[nextr][nextc]:
                        if curk==0:
                            pass
                        else:
                            visited.add((nextr,nextc))
                            queue.append((nextr,nextc,curk-1,curd+1))
                    else:
                        visited.add((nextr,nextc))
                        queue.append((nextr,nextc,curk,curd+1))
        return -1
'''

#attempt1: Committed same mistake again. Dont use DFS for shortest path!!!!!
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ans=[float('inf')]
        m,n=len(grid),len(grid[0])
        @lru_cache(None)
        def recurse(curr,curc,k):
            if curr>=m or curc>=n or curr<0 or curc<0:
                return float('inf')
            if curr==m-1 and curc==n-1:
                return 1
            if grid[curr][curc]:
                if k==0:
                    return float('inf')
                else:
                    ans[0]=min(ans[0],1+recurse(curr-1,curc,k-1),1+recurse(curr+1,curc,k-1),1+recurse(curr,curc+1,k-1),1+recurse(curr,curc-1,k-1))
            else:
                ans[0]=min(ans[0],1+recurse(curr-1,curc,k),1+recurse(curr+1,curc,k),1+recurse(curr,curc+1,k),1+recurse(curr,curc-1,k))
        recurse(0,0,k)
        return ans[0] if ans[0]!=float('inf') else -1
'''