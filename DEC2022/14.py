#attempt1:
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(None)
        def findAns(index):
            if index >= n:
                return 0
            return max(findAns(index+1), nums[index]+findAns(index+2))
        return findAns(0)
        
