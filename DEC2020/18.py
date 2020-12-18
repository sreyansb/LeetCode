#attempt1:
from heapq import heappop,heappush
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3:
            return False
        mins=[1]*n
        maxs=[1]*n
        for i in range(1,n):
            mins[i]=min(mins[i-1],nums[i-1])
        for j in range(n-2,-1,-1):
            maxs[j]=max(maxs[j+1],nums[j+1])
        for i in range(1,n-1):
            if mins[i]<nums[i]<maxs[i]:
                return True
        return False
                
        
            
        
