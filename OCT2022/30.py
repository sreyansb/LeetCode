#attempt2:
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        minans = [float('inf')]
        
        def findShortestPath(startRow,startCol,initialK):
            queue = deque([(0,0,initialK,0)])
            visited = {(0,0,initialK)}
            while(queue):
                #print(queue)
                row,col,curK,steps = queue.popleft()
                if (row,col) == (m-1,n-1):
                    if curK >= 0:
                        return steps
                    continue
                for nextRow,nextCol in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                    if not(0<=nextRow<m and 0<=nextCol<n):
                        continue
                    if grid[nextRow][nextCol]:
                        if curK <= 0:
                            continue
                    if (nextRow,nextCol,curK-grid[nextRow][nextCol]) in visited:
                        continue
                    visited.add((nextRow,nextCol,curK-grid[nextRow][nextCol]))
                    queue.append((nextRow,nextCol,curK-grid[nextRow][nextCol],steps+1))
            return -1
        
        return findShortestPath(0,0,k)
# 0 0
# 1 0
# 1 0
# 1 0
# 1 0
# 1 0
# 0 0
# 0 1
# 0 1
# 0 0
# 1 0
# 1 0
# 0 0

#attempt1:TLE
'''
from collections import deque
from heapq import heappush,heappop
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        minans = [float('inf')]
        
        def findShortestPath(startRow,startCol,initialK):
            queue = deque([(m-1,n-1,initialK,0)])
            visited = {(0,0,initialK)}
            while(queue):
                #print(queue)
                row,col,curK,steps = queue.popleft()
                if (row,col) == (0,0):
                    if curK >= 0:
                        return steps
                    continue
                for nextRow,nextCol in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                    if not(0<=nextRow<m and 0<=nextCol<n):
                        continue
                    if grid[nextRow][nextCol]:
                        if curK <= 0:
                            continue
                    if (nextRow,nextCol,curK-grid[nextRow][nextCol]) in visited:
                        continue
                    visited.add((nextRow,nextCol,curK-grid[nextRow][nextCol]))
                    queue.append((nextRow,nextCol,curK-grid[nextRow][nextCol],steps+1))
            return -1
        
        return findShortestPath(0,0,k)
# 0 0
# 1 0
# 1 0
# 1 0
# 1 0
# 1 0
# 0 0
# 0 1
# 0 1
# 0 0
# 1 0
# 1 0
# 0 0
'''
