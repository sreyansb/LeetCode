#attempt2: 63%
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def bsearch(nums,target):
            start,end=0,len(nums)-1
            while(start<=end):
                mid=(start+end)//2
                if nums[mid]==target:
                    return True
                if nums[mid]>target:
                    end=mid-1
                else:
                    start=mid+1
            return False
        index=-1
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                index=i
                break
        if index!=-1:
            nums=nums[index:]+nums[:index]
        return bsearch(nums,target)

#attempt1: 25%
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
'''
