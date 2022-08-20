#attempt1:
from heapq import heappush,heappop
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        currentFuel = startFuel
        availableFuel = []
        stops = 0
        stations.sort(key = lambda x:-x[0])
        currentPos = 0
        while(stations and currentPos < target):
            pos,fuel = stations.pop()
            if currentFuel + currentPos >= pos:
                currentFuel -= (pos-currentPos)
                currentPos = pos
                heappush(availableFuel,-fuel)
            else:
                if availableFuel:
                    highestFuel = -heappop(availableFuel)
                else:
                    return -1
                currentFuel += highestFuel
                stops += 1
                stations.append([pos,fuel])
        while(currentFuel+currentPos < target):
            if not(availableFuel):
                return -1
            currentFuel += -heappop(availableFuel)
            stops += 1
            
        return stops
                
            
            
            
