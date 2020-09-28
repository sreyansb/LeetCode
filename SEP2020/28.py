#attempt4: Sliding Window -similar intuition but no use of dp array and all
#quite easy it all depends on the array from initial to i
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==0:
            return 0
        count=0
        initial=0
        curprod=1
        for i in range(n):
            curprod*=nums[i]
            while(initial<i and curprod>=k):
                curprod/=nums[initial]
                initial+=1
            if curprod<k:
                count+=i-initial+1
        return count

#attempt3: Still TLE ->74/84
"""
from bisect import bisect_left
from math import ceil
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==0:
            return 0
        count=0
        nums=[0]+nums
        dp=[nums[1]] if nums[1]<k else []
        if dp:
            count+=1
        for i in range(2,n+1):
            if nums[i]<k:
                new=[nums[i]]
                if dp:
                    findindex = bisect_left(dp,ceil(k/nums[i]))
                    count+=findindex+1
                    #new+=[nums[i]*j for j in dp[:findindex]]
                    #copying the array is taking a lot of time
                dp=new
            else:
                dp=[]
            #print(i,nums[i],dp,count)
        return count
"""

#attempt2: TLE 74/84 tried changing a few stuff but isn't easy
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==0:
            return 0
        count=0
        nums=[0]+nums
        dp=[nums[1]] if nums[1]<k else []
        if dp:
            count+=1
        for i in range(2,n+1):
            if nums[i]<k:
                new=[]
                count+=1
                if dp and dp[0]*nums[i]<k:
                    count+=len(dp)
                    new=[nums[i]*j for j in dp]
                elif dp:
                    for j in dp:
                        if nums[i]*j<k:
                            count+=1
                            new.append(nums[i]*j)
                new.append(nums[i])
                dp=new
            else:
                dp=[]
            #print(i,count)
        return count
"""

#attempt1 TLE 74/84 quite an intuitive approach sliding window
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==0:
            return 0
        count=0
        nums=[0]+nums
        dp=[nums[1]] if nums[1]<k else []
        if dp:
            count+=1
        for i in range(2,n+1):
            if nums[i]<k:
                new=[]
                count+=1
                for j in dp:
                    if nums[i]*j<k:
                        count+=1
                        new.append(nums[i]*j)
                new.append(nums[i])
                dp=new
            else:
                dp=[]
            #print(i,count)
        return count
"""
