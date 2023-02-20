#attempt1: JUST COPIED PREVIOUS ATTEMPT
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n-1
        ans = -1
        while(start<=end):
            mid = (start+end)//2
            if nums[mid]<target:
                if mid+1<n and nums[mid+1]>=target:
                    return mid+1
                start = mid+1
            elif nums[mid]>target:
                end = mid-1
            else:
                ans = mid
                end = mid-1
        if ans == -1:
            if target<nums[0]:
                return 0
            elif target>nums[-1]:
                return n
        return ans
        
        
