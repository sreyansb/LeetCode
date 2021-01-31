#attempt3:93%
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        end=end1=len(nums)-1
        while(end>=1):
            if nums[end]>nums[end-1]:
                break
            end-=1
        if not(end):
            nums.sort()
            return
        while(end1>=end):
            if nums[end1]>nums[end-1]:
                break
            end1-=1
        nums[end-1],nums[end1]=nums[end1],nums[end-1]
        newend=len(nums)-1
        while(end<=newend):
            nums[end],nums[newend]=nums[newend],nums[end]
            end+=1
            newend-=1
        return
        

#attempt2:57%
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if sorted(nums,reverse=True)==nums:
            nums.sort()
            return
        end=end1=len(nums)-1
        while(end>=1):
            if nums[end]>nums[end-1]:
                break
            end-=1
        while(end1>=end):
            if nums[end1]>nums[end-1]:
                break
            end1-=1
        nums[end-1],nums[end1]=nums[end1],nums[end-1]
        newend=len(nums)-1
        while(end<=newend):
            nums[end],nums[newend]=nums[newend],nums[end]
            end+=1
            newend-=1
        return        
'''

#attempt1: WA: it is the rightmost element GREATER and not greater than or equal to
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if sorted(nums,reverse=True)==nums:
            nums.sort()
            return
        end=end1=len(nums)-1
        while(end>=1):
            if nums[end]>=nums[end-1]:
                break
            end-=1
        while(end1>=end):
            if nums[end1]>=nums[end-1]:
                break
            end1-=1
        nums[end-1],nums[end1]=nums[end1],nums[end-1]
        newend=len(nums)-1
        while(end<=newend):
            nums[end],nums[newend]=nums[newend],nums[end]
            end+=1
            newend-=1
        return
'''
