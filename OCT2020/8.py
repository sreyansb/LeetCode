class Solution:
    def search(self, nums, target):
        n=len(nums)
        if n==0:
            return -1
        start=0
        end=n-1
        while(start<=end):
            mid=start+(end-start)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                end=mid-1
            else:
                start=mid+1#write as start and not low
        return -1

obj=Solution()
print(obj.search([-1,0,3,5,9,12],9))
            
        
