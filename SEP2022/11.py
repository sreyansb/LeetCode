#attempt1: TOOK HELP
from heapq import heappush,heappop
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        speedEfficiency = zip(speed,efficiency)
        speedEfficiency = sorted(speedEfficiency,key = lambda x:x[1])
        #print(speedEfficiency)
        curSpeedSum, maxPerf = 0,0
        curStack = []
        curlen = 0
        for engSpeed,engEff in speedEfficiency[::-1]:
            curSpeedSum += engSpeed
            maxPerf = max(maxPerf,curSpeedSum*engEff)
            heappush(curStack,engSpeed)
            curlen += 1
            #print(curStack)
            if curlen == k:
                curSpeedSum -= heappop(curStack)
                curlen -= 1
            
        return maxPerf%(1000000007)
            
        
        
