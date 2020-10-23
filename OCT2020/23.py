#attempt4: 97.89% and 15.1MB
#took help from Channa sir
#we calculate the minimums from index(0 to i) for each valid index i
#then use a min heap to store every element that has been processed
#for every index i(0<i<n-1) we fix that as j, the min heap gives the element at index k
#nums[k]>nums[i] and nums[k]<nums[j], so keep popping from  min heap until heap[0]>nums[0..j-1]

from heapq import heappush,heappop
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3:
            return False
        mins=[nums[0]]
        for i in nums[1:]:
            mins.append(min(mins[-1],i))
        priorities=[]
        heappush(priorities,nums[-1])
        for i in range(n-2,0,-1):
            while(priorities and priorities[0]<=mins[i-1]):
                heappop(priorities)
            if priorities and priorities[0]<nums[i]:
                return True
            heappush(priorities,nums[i])
        return False
        

#attempt3: WA wrong idea
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3:
            return False
        def checkincreasing():
            for i in range(1,n):
                if nums[i]>=nums[i-1]:
                    continue
                else:
                    return False
            return True
        def checkdecreasing():
            for i in range(1,n):
                if nums[i]<=nums[i-1]:
                    continue
                else:
                    return False
            return True
        if checkincreasing() or checkdecreasing():
            return False
        return True
"""

#attempt2: TLE 94/96
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3:
            return False
        ans=False
        for i in range(n):
            j=i+1
            ran=[i,i]
            init=0
            while(j<n):
                if nums[j]>nums[i]:
                    if init==1:
                        if nums[j]<ran[1]:
                            ans=True
                            break
                        else:
                            ran[0],ran[1]=min(ran[0],nums[j]),max(ran[1],nums[j])
                    else:
                        init=1
                        ran[0],ran[1]=nums[j],nums[j]
                j+=1
            if ans:
                break            
        return ans
"""

#attempt1: WA 86/96 wrong because i didnt consider range
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3:
            return False
        ans=False
        for i in range(n):
            jflag,javalue=0,10**9+1
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    if not(jflag):
                        jflag=1
                        jvalue=nums[j]
                    else:
                        if nums[j]>nums[i] and nums[j]<jvalue:
                            ans=True
                            break
            if ans:
                break
        return ans
""" 
