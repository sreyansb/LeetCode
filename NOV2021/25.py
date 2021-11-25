#attempt2:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -float('inf')
        cursum = 0
        for i in range(n):
            cursum += nums[i]
            ans = max(ans,nums[i])
            if cursum<0:
                cursum = 0
            else:
                ans = max(ans,cursum)
        return ans

#attempt1:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = max(nums)
        cursum = 0
        for i in range(n):
            cursum += nums[i]
            if cursum<0:
                cursum = 0
            else:
                ans = max(ans,cursum)
        return ans
        
        
