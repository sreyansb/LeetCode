#attempt3: AC 99% because visited check only at the site of observation
from collections import deque
from sortedcontainers import SortedList
from heapq import heappush,heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        queue = []
        heap = []
        m,n = len(heights),len(heights[0])
        visited = set()
        heappush(heap,(0,0,0))
        
        while(heap):
            distance,x,y = heappop(heap)
            if x==m-1 and y==n-1:
                return distance
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if -1<x+1<m and (x+1,y) not in visited:
                heappush(heap,(max(distance,abs(heights[x+1][y]-heights[x][y])),x+1,y))
            if -1<x-1<m and (x-1,y) not in visited:
                heappush(heap,(max(distance,abs(heights[x-1][y]-heights[x][y])),x-1,y))
            if -1<y+1<n and (x,1+y) not in visited:
                heappush(heap,(max(distance,abs(heights[x][y+1]-heights[x][y])),x,y+1))
            if -1<y-1<n and (x,y-1) not in visited:
                heappush(heap,(max(distance,abs(heights[x][y-1]-heights[x][y])),x,y-1))
            #print(heap)
                
            
            

#attempt2: TLE because of visited check times
'''
from collections import deque
from sortedcontainers import SortedList
from heapq import heappush,heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        queue = []
        heap = []
        m,n = len(heights),len(heights[0])
        visited = set()
        heappush(heap,(0,0,0))
        
        while(heap):
            distance,x,y = heappop(heap)
            if x==m-1 and y==n-1:
                return distance
            visited.add((x,y))
            if -1<x+1<m and (x+1,y) not in visited:
                if (x+1,y) not in visited:
                    heappush(heap,(max(distance,abs(heights[x+1][y]-heights[x][y])),x+1,y))
            if -1<x-1<m and (x-1,y) not in visited:
                if (x-1,y) not in visited:
                    heappush(heap,(max(distance,abs(heights[x-1][y]-heights[x][y])),x-1,y))
            if -1<y+1<n and (x,1+y) not in visited:
                if (x,y+1) not in visited:
                    heappush(heap,(max(distance,abs(heights[x][y+1]-heights[x][y])),x,y+1))
            if -1<y-1<n and (x,y-1) not in visited:
                if (x,y-1) not in visited:
                    heappush(heap,(max(distance,abs(heights[x][y-1]-heights[x][y])),x,y-1))
            #print(heap)
'''

#attempt1: WA because of small typo in x and y final cell check
'''
from collections import deque
from sortedcontainers import SortedList
from heapq import heappush,heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        queue = []
        heap = []
        m,n = len(heights),len(heights[0])
        visited = set()
        heappush(heap,(0,0,0))
        
        while(heap):
            distance,x,y = heappop(heap)
            if x==n-1 and y==m-1:
                return distance
            visited.add((x,y))
            if -1<x+1<m and (x+1,y) not in visited:
                if (x+1,y) not in visited:
                    heappush(heap,(max(distance,abs(heights[x+1][y]-heights[x][y])),x+1,y))
            if -1<x-1<m and (x-1,y) not in visited:
                if (x-1,y) not in visited:
                    heappush(heap,(max(distance,abs(heights[x-1][y]-heights[x][y])),x-1,y))
            if -1<y+1<n and (x,1+y) not in visited:
                if (x,y+1) not in visited:
                    heappush(heap,(max(distance,abs(heights[x][y+1]-heights[x][y])),x,y+1))
            if -1<y-1<n and (x,y-1) not in visited:
                if (x,y-1) not in visited:
                    heappush(heap,(max(distance,abs(heights[x][y-1]-heights[x][y])),x,y-1))
            #print(heap)
'''
