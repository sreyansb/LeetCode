#attempt1:
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        currentSumOfEven = 0
        for num in nums:
            currentSumOfEven += num if num&1 == 0 else 0
        ans = [0]*(len(queries))
        curIndex = 0
        for addend,index in queries:
            if nums[index]&1 == 0:
                currentSumOfEven -= nums[index]
            nums[index] += addend
            if nums[index]&1 == 0:
                currentSumOfEven += nums[index]
            ans[curIndex] = currentSumOfEven
            curIndex += 1
        return ans
