#attempt2: 
from heapq import heappush,heappop
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        stack=[]
        curlen=1
        dp=[-float('inf') for i in range(n)]#max value with that index
        dp[n-1]=nums[-1]
        for i in range(n-1,-1,-1):
            while(stack and stack[0][1]-i>k):
                heappop(stack)
            if not stack:
                dp[i]=nums[i]
            else:
                dp[i]=nums[i]-stack[0][0]
            heappush(stack,(-dp[i],i))
            #print(stack)
        #print(dp)
        return dp[0]

#attempt1: WA didnt read the question properly: you need to reach index n-1 and not index n
'''
from heapq import heappush,heappop
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        stack=[]
        curlen=1
        dp=[-float('inf') for i in range(n)]#max value with that index
        dp[n-1]=nums[-1]
        heappush(stack,(0,n))
        for i in range(n-1,-1,-1):
            while(stack and stack[0][1]-i>k):
                heappop(stack)
            if not stack:
                dp[i]=nums[i]
            else:
                dp[i]=nums[i]-stack[0][0]
            heappush(stack,(-dp[i],i))
            #print(stack)
        #print(dp)
        return dp[0]
'''