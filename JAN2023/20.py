#attempt1:
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        @lru_cache(None)
        def dfs(index):
            if index >= n:
                []
            ans = [[nums[index]]]
            for nextIndex in range(index+1,n):
                if nums[nextIndex] >= nums[index]:
                    for newAns in dfs(nextIndex):
                        ans.append([nums[index]] + newAns)
            return ans
        def filterFun(listOfEles):
            return len(listOfEles) > 1
        ans = []
        for index in range(n):
            soln = dfs(index)
            ans += soln
        return list(filter(filterFun, set([tuple(i) for i in ans])))
