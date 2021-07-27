#attempt2: TWO POINTER APPROACH always for 3sum use 2 pointer approach
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        mindiff=float('inf')
        sumatdiff=float('inf')
        nums.sort()
        for i in range(n):
            start=i+1
            end=n-1
            while(start<end):
                if nums[i]+nums[start]+nums[end]<target:
                    if mindiff>abs(nums[i]+nums[start]+nums[end]-target):
                        mindiff=abs(nums[i]+nums[start]+nums[end]-target)
                        sumatdiff=nums[i]+nums[start]+nums[end]
                    start+=1
                else:
                    if mindiff>abs(nums[i]+nums[start]+nums[end]-target):
                        mindiff=abs(nums[i]+nums[start]+nums[end]-target)
                        sumatdiff=nums[i]+nums[start]+nums[end]
                    end-=1
        return sumatdiff
                    
# attempt1: TLE used naive approach but didnt work
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        mindiff=float('inf')
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    newdiff=abs(nums[i]+nums[j]+nums[k]-target)
                    if newdiff<mindiff:
                        mindiff=newdiff
                        sumatdiff=nums[i]+nums[j]+nums[k]
        return sumatdiff
'''