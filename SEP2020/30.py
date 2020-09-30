#attempt2: requirements is O(N) and O(1) took help, quite a nice approach
#using some knowledge of range and allowable answers
#constant space - took help
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        has1=0
        n=len(nums)
        #the missing number can only lie between 1 and len(nums)+1
        for i in range(n):
            if nums[i]==1:
                has1=1
            if nums[i]<1 or nums[i]>n:
                nums[i]=1
            
        if has1==0:
            return 1
        ans=2
        #print(nums)
        for i in nums:
            if abs(i)-1>-1 and nums[abs(i)-1]>0:
                nums[abs(i)-1]*=-1
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1

#attempt1: O(n) algo Extra O(N) space
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not(nums):
            return 1
        di={}
        maxi=max(nums)
        for i in nums:
            if i>0:
                di[i]=1
        for i in range(1,maxi+1):
            if i not in di:
                return i
        return max(1,maxi+1)
"""
