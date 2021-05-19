#attempt2: TOOK HELP: IT is about finding the median
#such problems are usually about finding the median or the mean
#try either and check, very important
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n%2:
            median=nums[n//2]
            return sum([abs(i-median) for i in nums])
        else:
            median=(nums[n//2]+nums[(n//2)-1])//2
            return sum([abs(i-median) for i in nums])

#attempt1:WA First tried thinking about mean.
#  tried to do binary search from 10^-9 to 10^9 to find the number
#doesn't work
'''
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def calcnums(val):
            ans=0
            for i in nums:
                ans+=abs(i-val)
            return ans
        low=10**(-9)
        high=10**(9)
        dp={}
        mini=float('inf')
        while(low<high):
            mid=(low+high)//2
            if mid==low or mid==high:
                break
            if mid not in dp:
                dp[mid]=calcnums(mid)
            if low not in dp:
                dp[low]=calcnums(low)
            if high not in dp:
                dp[high]=calcnums(high)
            mini=min(mini,dp[mid])
            if dp[low]<=dp[high]:
                high=mid
            else:
                low=mid
        return int(mini)
        
'''