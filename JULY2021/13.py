#attempt1: Very easy: Remember to return i-1 and not i
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        newarr=[-float('inf')]+nums+[-float('inf')]
        for i in range(1,len(newarr)-1):
            if newarr[i-1]<newarr[i] and newarr[i]>newarr[i+1]:
                return i-1
        return -1
        
        