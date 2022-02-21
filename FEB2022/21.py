#attempt1:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        floor_div = n//2
        while(i<n):
            ele = nums[i]
            count = 0
            while(i<n and nums[i]==ele):
                count += 1
                i += 1
            if count > floor_div:
                return ele
        return -1
