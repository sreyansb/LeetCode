from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        ans=[]
        for i in range(n):
            pos=bisect_left(ans,nums[i])
            if pos==len(ans):
                ans.append(i)
            ans[pos]=nums[i]
        return len(ans)
        
        
