#attempt 3
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        li=[]
        i=0
        while(i<len(nums)):
            ele=nums[i]
            j=i+1
            while(j<len(nums) and nums[j]==ele):
                j+=1
            if j-i-1:
                li.append(ele)
            i=j
        return li

#Attempt 2
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        di={}
        for i in nums:
            if i not in di:
                di[i]=0
            di[i]+=1
        l=[]
        for i in di:
            if di[i]>1:
                l.append(i)
        return l
"""

#Attempt 1
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        di={}
        l=set()
        for i in nums:
            if i not in di:
                di[i]=0
            di[i]+=1
            if di[i]>1:
                l.add(i)
        return list(l)
"""          
        
        
