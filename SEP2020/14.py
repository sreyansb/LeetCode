#attempt 2: 40% and 90% -> if we use lists

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not(nums):
            return 0
        n=len(nums)
        dp=[-1 for i in range(n)]
        def dpkaro(index,cost):
            #print(index,cost)
            if index>=n:
                return 0+cost
            if dp[index]!=-1:
                return dp[index]+cost
            dp[index]=max(dpkaro(index+1,cost),dpkaro(index+2,cost+nums[index]))
            return dp[index]
        return dpkaro(0,0)


#attempt 1: WA very bad thinking
#you cant just return dp[index] or 0, we need to add the previous costs to it.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not(nums):
            return 0
        n=len(nums)
        dp=[-1 for i in range(n)]
        def dpkaro(index,cost):
            #print(index,cost)
            if index>=n:
                return 0
            if dp[index]!=-1:
                return dp[index]
            dp[index]=max(dpkaro(index+1,cost),dpkaro(index+2,cost+nums[index]))
            return dp[index]
        return dpkaro(0,0)
"""
