#attempt1:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        multi = [1 for i in range(n)]
        for i in range(1,n):
            multi[i] *= nums[i-1]*multi[i-1]
        curpdt = 1
        for i in range(n-2,-1,-1):
            curpdt *= nums[i+1]
            multi[i] *= curpdt
        return multi
        
