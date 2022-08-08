#attempt1:
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [0]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    LIS[i] = max(LIS[i],LIS[j]+1)
        return max(LIS)+1
        
