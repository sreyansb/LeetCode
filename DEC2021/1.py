#attempt2: 28ms
class Solution:
    def rob(self, nums: List[int]) -> int:
        end = len(nums)
        @lru_cache(None)
        def robbery(start):
            if start>=end:
                return 0
            return max(robbery(start+1),nums[start]+robbery(start+2))
        return robbery(0)
        

#attempt1: TLE 48/68: NO lru caching
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums:
            return max(self.rob(nums[1:]),nums[0]+self.rob(nums[2:]))
        return 0
'''
