#attempt1: 98% and 80%
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)-1
        i=n
        j=n
        if nums==sorted(nums,reverse=True):
            start,end=0,n
            while(start<=end):
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
            return nums
        while(i>0):
            if nums[i]>nums[i-1]:
                break
            i-=1
        while(j>=i):
            if nums[j]>nums[i-1]:
                break
            j-=1
        nums[i-1],nums[j]=nums[j],nums[i-1]
        start=i
        end=n
        while(start<=end):
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
        return nums
        
        
