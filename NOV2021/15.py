#attempt2:
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        indices = [i for i in range(n)]
        maxl = [1 for i in range(n)]
        #print(nums)
        for i in range(1,n):
            maxc = 1
            index = i
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    maxc = max(maxl[j]+1,maxc)
                    if maxc == maxl[j]+1 :
                        index = j
            maxl[i] = maxc
            indices[i] = index
        #print(maxl)
        #print(indices)
        finali = maxl.index(max(maxl))
        ans = []
        while(indices[finali]!=finali):
            ans.append(nums[finali])
            finali = indices[finali]
        ans.append(nums[finali])
        return ans

#attempt1: TOOK HINT, no idea how to solve  WA overlooked indices[i] = j.
#SHould be index
#LIS BASED PROBLEM
'''
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        indices = [i for i in range(n)]
        maxl = [1 for i in range(n)]
        for i in range(1,n):
            maxc = 1
            index = i
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    maxc = max(maxl[j]+1,maxc)
                    if maxc == maxl[j]+1 :
                        index = j
            maxl[i] = maxc
            indices[i] = j
        finali = maxl.index(max(maxl))
        ans = []
        while(indices[finali]!=finali):
            ans.append(nums[finali])
            finali = indices[finali]
        ans.append(nums[finali])
        return ans
'''