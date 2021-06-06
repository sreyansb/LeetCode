#attempt3: USED DP: HAVE a visited array for dp or lru_cache
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        @lru_cache(None)
        def dp(x):
            if x-1 in nums:
                return dp(x-1)+1
            return 1
        maxie=0
        for i in nums:
            maxie=max(maxie,dp(i))
        return maxie

#attempt2:Used sorting and set(nums)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=set(nums)
        nums=sorted(nums)
        maxie=1
        curlen=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                curlen+=1
            else:
                curlen=1
            maxie=max(maxie,curlen)
        return maxie
'''

#attempt1:It is WA because I didn't take into consideration that they wanted
#longest increasing subsequence and not substring
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        maxie=1
        curlen=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                curlen+=1
            else:
                curlen=1
            maxie=max(maxie,curlen)
        return maxie
'''
