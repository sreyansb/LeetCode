#attempt1:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        end = len(nums)-1
        while(low<=end):
            mid = (low+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                low = mid+1
            else:
                end = mid-1
        return -1
        
