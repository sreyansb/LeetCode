#attempt3:Took help: educative.io -actually copied the code.
#quite difficult to implement dp approach
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k=sum(nums)
        n=len(nums)
        if k%2:
            return False
        k=k//2
        #we need to try making all sums possible with j elements
        #dp[j][i] represents if we can make sum i with j elements
        dp=[[False for i in range(k+1)]for i in range(n)]
        for i in range(n):#make sum 0 with i elements->always possible by not taking any
            dp[i][0]=True
        for i in range(1,k+1):#can we make sum i with 0th elements
            dp[0][i]=nums[0]==k
        for i in range(1,n):
            for j in range(1,k+1):
                if dp[i-1][j]:
                    dp[i][j]=dp[i-1][j]
                elif nums[i]<=j:
                    dp[i][j]=dp[i-1][j-nums[i]]
        return dp[n-1][k]

#attempt2: Reduced from 2^n to 2^(n/2) -> would still give TLE
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        curlevel=[(nums[0],0)]
        for i in range(1,n):
            nextlevel=[]
            for j in curlevel:
                nextlevel.append((j[0]+nums[i],j[1]))
                nextlevel.append((j[0],j[1]+nums[i]))
            curlevel=nextlevel.copy()
        for i in curlevel:
            if i[0]==i[1]:
                return True
        return False        
'''
#attempt1: TLE 36/115
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        def recurse(index,firstg=[],secondg=[]):
            if index>n:
                return False
            if index==n:
                if sum(firstg)==sum(secondg):
                    return True
                return False
            return recurse(index+1,firstg+[nums[index]],secondg) or recurse(index+1,firstg,secondg+[nums[index]])
        return recurse(0)
'''
