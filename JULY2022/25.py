#attempt2:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [float('inf'),-float('inf')]
        def binSearch(startAddend,endAddend,nums = nums):
            start,end = 0,len(nums)-1
            while(start <= end):
                mid = (start+end)//2
                if nums[mid] == target:
                    ans[0] = min(ans[0],mid)
                    ans[1] = max(ans[1],mid)
                    start += startAddend
                    end += endAddend
                elif nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
        binSearch(0,-1)
        binSearch(1,0)
        if ans[0] == float('inf'):
            return [-1,-1]
        return ans     

#attempt1:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        start,end = 0,len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if nums[mid] == target:
                ans[0] = mid
                end = mid-1
            elif nums[mid] < target:
                start  = mid+1
            else:
                end = mid-1
        start,end = 0,len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if nums[mid] == target:
                ans[1] = mid
                start = mid+1
            elif nums[mid] < target:
                start  = mid+1
            else:
                end = mid-1
        return ans
        
