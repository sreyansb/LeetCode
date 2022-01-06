#attempt1: 60ms
from heapq import heappush,heappop
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap_of_trips = []
        for i in trips:
            heappush(heap_of_trips,(i[1],i[0]))
            heappush(heap_of_trips,(i[2],-i[0]))
        curcap = 0
        while(heap_of_trips):
            if curcap>capacity:
                return False
            curcap += heappop(heap_of_trips)[1]
        return True
        
        
