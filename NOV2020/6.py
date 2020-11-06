#attempt1: 82%, took hint, very easy problem
#get all factors that are possible of the list nums and finish based on that
from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            k=sum([ceil(i/mid) for i in nums])
            if k<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
                    
            
            
        
