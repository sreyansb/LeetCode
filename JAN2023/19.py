#attempt1: TOOK HELP
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        freq = {}
        for kmod in range(k):
            freq[kmod] = 0
        freq[0] = 1
        ans = 0
        runningSum = 0
        for ele in nums:
            runningSum += ele
            remainder = runningSum%k
            ans += freq[remainder]
            freq[remainder] += 1
        return ans


        
