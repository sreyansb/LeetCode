#attempt1:
from bisect import bisect_right
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for index in range(1,len(nums)):
            nums[index] += nums[index-1]
        ans = []
        for query in queries:
            ans.append(bisect_right(nums,query))
        return ans
