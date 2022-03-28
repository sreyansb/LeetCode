#attempt1:
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums_len = len(nums)
        def recurse(low,high):
            if low>high:
                return False
            mid = (low+high)//2
            return nums[mid] == target or recurse(low,mid-1) or recurse(mid+1,high)
        return recurse(0,nums_len-1)
                
                
            
