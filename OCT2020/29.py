#attempt2: 86% took help
#-> count 0s between 1's. it will be in center of the string of 0s
#if enclosed by 1's, if 00000...1, it will be curd
#if 1....000000, it will be curd
from math import ceil
class Solution:
    def maxDistToClosest(self, nums: List[int]) -> int:
        maxd=1
        curd=0
        n=len(nums)
        index=0
        hasone=0
        while(index<n):
            if nums[index]:
                if hasone:
                    maxd=max(maxd,ceil(curd/2))
                else:
                    hasone=1
                    maxd=max(maxd,curd)
                curd=0
            else:
                curd+=1
            index+=1
        return max(maxd,curd)
        
        

#attempt1: 40%
"""
class Solution:
    def maxDistToClosest(self, nums: List[int]) -> int:
        n=len(nums)
        k=float('inf')
        leftdis=[0 for i in range(n)]
        rightdis=[0 for i in range(n)]
        if nums[0]==0:
            leftdis[0]=k
        if nums[-1]==0:
            rightdis[-1]=k
        for i in range(1,n):
            if nums[i]==1:
                leftdis[i]=0
            else:
                leftdis[i]=leftdis[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]==1:
                rightdis[i]=0
            else:
                rightdis[i]=rightdis[i+1]+1
        mins=[min(leftdis[i],rightdis[i]) for i in range(n)]
        return max(mins)
"""
