#attempt2:
from typing import *
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di1={}
        di2={}
        for i in nums1:
            if i not in di1:
                di1[i]=0
            di1[i]+=1
        for i in nums2:
            if i not in di2:
                di2[i]=0
            di2[i]+=1
        ans=[]
        for i in di1:
            try:
                ans.extend([i]*(min(di1[i],di2[i])))
            except:
                pass
        return ans

#attempt1:
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di1={}
        di2={}
        for i in nums1:
            if i not in di1:
                di1[i]=0
            di1[i]+=1
        for i in nums2:
            if i not in di2:
                di2[i]=0
            di2[i]+=1
        ans=[]
        for i in set(di1)&set(di2):
            ans.extend([i]*(min(di1[i],di2[i])))
        return ans
'''