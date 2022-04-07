#attempt1:
from heapq import heapify,heappush,heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapify(heap)
        while(len(heap)!=1):
            ele1 = -heappop(heap)
            ele2 = -heappop(heap)
            heappush(heap,-ele1+ele2)
        return -heap[0]
