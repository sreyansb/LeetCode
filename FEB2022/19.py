#attempt3: Copied previous attempt
from heapq import heapify,heappush,heappop
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        eles=list(set([-i*2 if i&1 else -i for i in nums]))
        heapify(eles)
        maxi,mini=-eles[0],-max(eles)
        diff=maxi-mini
        while(-(eles[0])&1==0):
            m=heappop(eles)//2
            heappush(eles,m)
            mini=min(mini,-m)
            maxi=-eles[0]
            diff=min(diff,maxi-mini)
        return diff
