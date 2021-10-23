#attempt3: Random O(n) solution for recursion
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        def recurse(low,end):
            if low<=end:
                mid = (low+end)//2
                return min(nums[mid],recurse(low,mid-1),recurse(mid+1,end))
            return float('inf')
        return recurse(0,n-1)

#attempt2: WA Minimum could be on either side of the mid
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        def recurse(low,end):
            if low<=end:
                mid = (low+end)//2
                ans = nums[mid]
                if mid+1<n and nums[mid]>=nums[mid+1]:
                    ans = min(ans,recurse(mid+1,end))
                if mid-1>-1 and nums[mid]>=nums[mid-1]:
                    ans = min(ans,recurse(low,mid-1))
                return ans
            return float('inf')
        return recurse(0,n-1)
'''


#attempt1: AC Just return min bro!
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
'''