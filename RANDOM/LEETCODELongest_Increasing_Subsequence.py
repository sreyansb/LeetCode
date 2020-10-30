class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        lic=[1 for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    lic[i]=max(lic[i],lic[j]+1)
        return max(lic)
        
        
