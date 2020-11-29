#attempt2: Took help from LEETCODE. Nice problem, easy to think but took help
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)-1
        for i in range(n,-1,-1):
            if i+nums[i]>=n:
                n=i
        return n==0

#attempt1: TLE 74/75
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)-1
        dp={}
        def dfs(index):
            if index>n:
                return False
            if index==n:
                return True
            if index in dp:
                return dp[index]
            ans=False
            for i in range(1,nums[index]+1):
                ans=dfs(index+i)
                if ans:
                    dp[index]=ans
                    return ans
            dp[index]=ans
            return ans
        return dfs(0)
'''
