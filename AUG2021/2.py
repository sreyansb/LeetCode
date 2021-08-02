#attempt1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for i in range(len(nums)):
            if target-nums[i] in di:
                return [i,di[target-nums[i]]]
            di[nums[i]]=i
        return [-1,-1]