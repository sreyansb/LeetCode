#attempt1:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def findAns(index):
            if index >= n:
                return False
            if index == n-1:
                return True
            if index + nums[index] >= n-1:
                return True
            ans = False
            for nextIndex in range(index+nums[index],index,-1):
                ans = ans or findAns(nextIndex)
            return ans
        
        return  findAns(0)
        
