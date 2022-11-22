#attempt1:
from bisect import bisect_right
from collections import deque
from heapq import heappush, heappop
class Solution:
    def numSquares(self, n: int) -> int:
        allSquares = []
        highest = 15000
        baseNumber = 1
        square = 0
        while(square <= highest):
            square = baseNumber * baseNumber
            allSquares.append(square)
            baseNumber += 1
        def bfs(n):
            heap = []
            heappush(heap,(0,n))
            #queue.append((n,0))
            while(heap):
                steps,element = heappop(heap)
                if element == 0:
                    return steps
                pos = bisect_right(allSquares, element)
                for square in allSquares[:pos]:
                    heappush(heap,(steps+(element//square),element%square))
            return -1
        return bfs(n)
