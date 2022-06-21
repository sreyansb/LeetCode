#attempt1:
from heapq import heappush, heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        for index in range(len(heights)-1):
            if heights[index+1] - heights[index] <= 0:
                continue
            bricks -= (heights[index+1]-heights[index])
            heappush(max_heap,heights[index]-heights[index+1])
            while(bricks<0 and ladders):
                bricks += -heappop(max_heap)
                ladders -= 1
            if ladders == 0 and bricks<0:
                return index
        return len(heights)-1
                
            
        
        
