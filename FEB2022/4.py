#attempt3: 1000ms
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #first observation : length can only be even
        n = len(nums)
        cursum = 0        
        di = {0:[-1]}
        maxl = 0
        for j in range(n):
            cursum += 1 if nums[j] else -1
            if cursum in di:
                for i in di[cursum]:
                    if (j-i)%2==0:
                        maxl = max(maxl,(j-i))
                        break
            else:
                di[cursum] = []
            di[cursum].append(j)        
        return maxl

#attempt2: 2073ms
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #first observation : length can only be even
        n = len(nums)
        zeros = [0 for i in range(n)]
        ones = [0 for i in range(n)]
        if nums[0]:
            ones[0] = 1
        else:
            zeros[0] = 1
        for i in range(1,n):
            ele = nums[i]
            ones[i] = ones[i-1] + ele
            zeros[i] = zeros[i-1] + (ele^1)
        di = {0:[-1]}
        maxl = 0
        for j in range(n):
            if ones[j]-zeros[j] in di:
                for i in di[ones[j]-zeros[j]]:
                    if (j-i)%2==0:
                        maxl = max(maxl,(j-i))
                        break
            else:
                di[ones[j]-zeros[j]] = []
            di[ones[j]-zeros[j]].append(j)        
        return maxl

#attempt1: TLE
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #first observation : length can only be even
        n = len(nums)
        zeros = [0 for i in range(n)]
        ones = [0 for i in range(n)]
        if nums[0]:
            ones[0] = 1
        else:
            zeros[0] = 1
        for i in range(1,n):
            ele = nums[i]
            ones[i] = ones[i-1] + ele
            zeros[i] = zeros[i-1] + (ele^1)
        
        maxl = 0
        for i in range(n):
            for j in range(i+1,n,2):
                if ones[j]-ones[i-1]==zeros[j]-zeros[i-1] if i>0 else ones[j]==zeros[j]:
                    maxl = max(maxl,j-i+1)
        return maxl
'''
