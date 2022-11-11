#attempt1:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        startIndex = 0
        prevElement = float('inf')
        numberOfDashes = 0
        for num in nums:
            if num == prevElement:
                numberOfDashes += 1
            else:
                nums[startIndex] = num
                startIndex += 1
            prevElement = num
        return startIndex
