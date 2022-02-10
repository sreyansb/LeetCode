#attempt1: cursum-k because cursum includes the previous sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di = {}
        di[0] = 1
        cursum =  0
        ans = 0
        for i in nums:
            cursum += i
            if cursum-k in di:
                ans += di[cursum-k]
            if cursum not in di:
                di[cursum] = 0
            di[cursum] += 1
        return ans
