#attempt2: Just copied
class Solution:
	def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

		length = len(multipliers)

		dp = [[0] * (length + 1) for _ in range(length + 1)]

		for multi in range(length - 1, -1, -1):

			for index in range(multi, -1, -1):

				left_output = multipliers[multi] * nums[index] + dp[multi + 1][index + 1]
				right_output = multipliers[multi] * nums[len(nums) - 1 - multi + index] + dp[multi + 1][index]
				dp[multi][index] = max(left_output, right_output)

		return dp[0][0]

#attempt1: TLE and Memory Error
'''
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        @lru_cache(None)
        def dfs(index,start,end):
            if index >= m:
                return 0
            if start > end:
                return -float('inf')
            return max(
                multipliers[index]*nums[start]+dfs(index+1,start+1,end),
                multipliers[index]*nums[end]+dfs(index+1,start,end-1)
            )
        return dfs(0,0,len(nums)-1)
'''
