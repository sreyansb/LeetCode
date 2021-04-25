#attempt1:
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        prev=0
        tot=0
        nums=nums+nums
        for i in range(n):
            prev+=i*nums[i]
            tot+=nums[i]
        maxie=prev
        for i in range(1,n):
            cur=prev-tot+n*nums[i-1]
            maxie=max(maxie,cur)
            prev=cur
        return maxie
