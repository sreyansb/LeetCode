#attempt3: AC took help 99.52%
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n=len(timeSeries)
        index=0
        maxi=0
        initial=0
        while(index<n):
            maxi+=min(duration,timeSeries[index]-initial+duration)
            initial=timeSeries[index]+duration 
            index+=1
        return maxi
        

#attempt2: WA TLE
"""
from bisect import bisect_left
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n=len(timeSeries)
        index=0
        maxi=0
        overlap=0
        while(index<n):
            pos=bisect_left(timeSeries,timeSeries[index]+duration-1)
            #print(index,pos)
            if pos<n:
                if timeSeries[index]+duration-1==timeSeries[pos]:
                    overlap=1
                    maxi+=duration
                    index=pos
                else:
                    maxi+=duration
                    index=pos
            else:
                maxi+=duration
                index=pos
        return maxi-overlap
"""       

#attempt1: TRIED
"""
from bisect import bisect_left
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n=len(timeSeries)
        index=0
        maxi=0
        while(index<n):
            pos=bisect_left(timeSeries,timeSeries[index]+duration-1)
            if pos<n:
                if timeSeries[index]+duration-1==timeSeries[pos]:
                    maxi+=duration
                    index=pos
                else:
                    maxi+=duration
                    index=pos
            else:
                maxi+=duration
                index=pos
        return maxi
"""
