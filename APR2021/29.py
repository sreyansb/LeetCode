#attempt1:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=[-1]
        right=[-1]
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]==target:
                if right[0]==-1:
                    right[0]=mid
                left[0]=mid
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        x=-1
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]==target:
                if x==-1:
                    x=mid
                right[0]=mid
                start=mid+1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return [left[0],right[0]]
                
                
            
