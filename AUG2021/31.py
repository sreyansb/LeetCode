#attempt1: Took Hint : Thought to make O(n) algo
#but then realized that O(logN) binary search is possible
#if  element at mid > element at end => lesser element will be from mid+1 to end
#else lesser element will lie in low to mid-1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        end=len(nums)-1
        ans=5001
        while(low<=end):
            mid=(low+end)//2
            if nums[mid]>nums[end]:
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                end=mid-1
        return ans
        