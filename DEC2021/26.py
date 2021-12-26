#attempt2: NSK's approach
from heapq import heapify,heappush,heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [(-(x[0]*x[0]+x[1]*x[1]),x) for x in points[:k]]
        heapify(minheap)
        print(minheap)
        for i in points[k:]:
            dist = -(i[0]*i[0]+i[1]*i[1])
            #print(dist)
            if dist>minheap[0][0]:
                heappop(minheap)
                heappush(minheap,(dist,i))
        return [i[1] for i in minheap]

#attempt1: simple one liner
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x:x[0]*x[0]+x[1]*x[1])
        return points[:k]
        
