#attempt4:
from heapq import  heappush,heappop
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        heap = []
        heappush(heap,[0,(0,0)])
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        visited = set()
        while(heap):
            #print(heap)
            dist,coord = heappop(heap)
            if tuple(coord) in visited:
                continue
            if coord[0] == n-1 and coord[1] == n-1:
                return dist+1
            visited.add(tuple(coord))
            for xdiff in [coord[0]-1,coord[0],coord[0]+1]:
                for ydiff in [coord[1]-1,coord[1],coord[1]+1]:
                    if (xdiff == coord[0] and ydiff == coord[1]) or not(0<=xdiff<n) or not(0<=ydiff<n) or grid[xdiff][ydiff] == 1:
                        continue
                    #print(xdiff,ydiff,coord)
                    heappush(heap,(dist+1,[xdiff,ydiff]))
        return -1

#attempt3: WA
'''
from heapq import  heappush,heappop
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        heap = []
        heappush(heap,[0,(0,0)])
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        final = (n-1,n-1)
        visited = set()
        while(heap):
            #print(heap)
            dist,coord = heappop(heap)
            if tuple(coord) in visited:
                continue
            if coord == final:
                return dist+1
            visited.add(tuple(coord))
            for xdiff in [coord[0]-1,coord[0],coord[0]+1]:
                for ydiff in [coord[1]-1,coord[1],coord[1]+1]:
                    if (xdiff,ydiff) == coord or not(0<=xdiff<n) or not(0<=ydiff<n) or grid[xdiff][ydiff] == 1:
                        continue
                    #print(xdiff,ydiff,coord)
                    heappush(heap,(dist+1,[xdiff,ydiff]))
        return -1
'''

#attempt2: WA because of some internal python issue
'''
from heapq import  heappush,heappop
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        heap = []
        heappush(heap,[0,(0,0)])
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        final = [n-1,n-1]
        visited = set()
        while(heap):
            dist,coord = heappop(heap)
            if tuple(coord) in visited:
                continue
            if coord == final:
                return dist+1
            visited.add(tuple(coord))
            for xdiff in [coord[0]-1,coord[0],coord[0]+1]:
                for ydiff in [coord[1]-1,coord[1],coord[1]+1]:
                    if [xdiff,ydiff] == coord or not(0<=xdiff<n) or not(0<=ydiff<n) or grid[xdiff][ydiff] == 1:
                        continue
                    heappush(heap,(dist+1,[xdiff,ydiff]))
        return -1
'''

#attempt1: TLE because visited vertex might be visited multiple times
'''
from heapq import  heappush,heappop
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        heap = []
        heappush(heap,[0,(0,0)])
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        final = [n-1,n-1]
        while(heap):
            dist,coord = heappop(heap)
            if coord == final:
                return dist+1
            for xdiff in [coord[0]-1,coord[0],coord[0]+1]:
                for ydiff in [coord[1]-1,coord[1],coord[1]+1]:
                    if [xdiff,ydiff] == coord or not(0<=xdiff<n) or not(0<=ydiff<n) or grid[xdiff][ydiff] == 1:
                        continue
                    heappush(heap,(dist+1,[xdiff,ydiff]))
        return -1
'''
