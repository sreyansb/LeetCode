#attempt1:
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        double=-1
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                double=nums[i]
                break
        return [double,(n*(n+1))//2-sum(nums)+double]
