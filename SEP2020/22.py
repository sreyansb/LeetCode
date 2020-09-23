#attempt1 - used nlogn  instead of n and space was o(1)->at the most 3 elemnts
from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        n=floor(len(nums)/3)
        count=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
            else:
                if count>n:
                    ans.append(nums[i-1])
                count=1
        if len(nums) and count>n:
            ans.append(nums[-1])
        return ans
