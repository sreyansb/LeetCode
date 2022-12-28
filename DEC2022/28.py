#attempt1:
from heapq import heapify, heappop, heappush
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        currentSum = sum(piles)
        maxHeap = [-i for i in piles]
        heapify(maxHeap)
        while(k):
            #print(maxHeap)
            element = -1 * heappop(maxHeap)
            currentSum -= element
            newElement = ceil(element/2)
            currentSum += newElement
            heappush(maxHeap, -(newElement))
            #print(currentSum)
            k -= 1
            
        return currentSum
