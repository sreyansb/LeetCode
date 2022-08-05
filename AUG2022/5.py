#attempt1:
from bisect import bisect_right
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        @lru_cache(None)
        def findans(target):
            if target == 0:
                return 1
            ans = 0
            pos = bisect_right(nums,target)
            for eles in nums[:pos]:
                ans += findans(target-eles)
            return ans
        return findans(target)
                
            
            
        
