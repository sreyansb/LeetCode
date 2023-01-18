#attempt5: Copied See attempts
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)

        cur_max=nums[0]
        ans=cur_max

        cur_min=nums[0]
        minans=cur_min

        for i in range(1,n):
            if cur_max<0:cur_max=nums[i]
            else:cur_max+=nums[i]
            ans=max(ans,cur_max)

            if cur_min>-1:cur_min=nums[i]
            else:cur_min+=nums[i]
            minans=min(minans,cur_min)

        if sum(nums)==minans:return ans
        return max(ans,sum(nums)-minans)
