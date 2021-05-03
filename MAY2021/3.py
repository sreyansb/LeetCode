#attempt1:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running=[nums[0]]
        for i in nums[1:]:
            running.append(running[-1]+i)
        return running
