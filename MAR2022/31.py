#attempt5: The last test case was special wherein we had to use the non-negative
#property such that if number_of_elements_greater_than_0<m => max has to returned
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        numbers_greater_than_0 = len([i for i in nums if i>0])
        if n == m or (numbers_greater_than_0<m):
            return max(nums)
        sums = [0]*n
        sums[0] = nums[0]
        for i in range(1,n):
            sums[i] = sums[i-1] + nums[i]
        if m==1 :
            return sums[-1]
        
        @lru_cache(None)
        def recurse(index,m):#at index how many cuts are remaining
            if m==1:
                return sums[-1] - (sums[index-1] if index>0 else 0)
            if n-index<m:
                return -float('inf')
            if n-index == m:
                return max(nums[index:])
            ans = float('inf')
            tosubtract = sums[index-1] if index>0 else 0
            p = -1
            for i in range(index,n-m+1):
                ans = min(ans,max(sums[i]-tosubtract,recurse(i+1,m-1)))
            return ans
        return recurse(0,m)
            
#attempt4: TLE
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if n == m:
            return max(nums)
        sums = [0]*n
        sums[0] = nums[0]
        for i in range(1,n):
            sums[i] = sums[i-1] + nums[i]
        if m==1 :
            return sums[-1]
        @lru_cache(None)
        def recurse(index,m):#at index how many cuts are remaining
            if m==1:
                return sums[-1] - (sums[index-1] if index>0 else 0)
            if n-1-index+1<m:
                return -float('inf')
            if n-1-index+1 == m:
                return max(nums[index:])
            ans = float('inf')
            tosubtract = sums[index-1] if index>0 else 0
            p = -1
            for i in range(index,n-m+1):
                ans = min(ans,max(sums[i]-tosubtract,recurse(i+1,m-1)))
            return ans
        return recurse(0,m)
'''

#attempt3:  WA because we have to iterate in i loop only till n-m
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if n == m:
            return max(nums)
        sums = [0]*n
        sums[0] = nums[0]
        for i in range(1,n):
            sums[i] = sums[i-1] + nums[i]
        if m==1 :
            return sums[-1]
        m -= 1
        @lru_cache(None)
        def recurse(index,m):#at index how many cuts are remaining
            if m==0:
                return sums[-1] - (sums[index-1] if index>0 else 0)
            if n-1-index+1<m+1:
                return -float('inf')
            if n-1-index+1 == m+1:
                return max(nums[index:])
            ans = float('inf')
            tosubtract = sums[index-1] if index>0 else 0
            p = -1
            for i in range(index,n):
                ans = min(ans,max(sums[i]-tosubtract,recurse(i+1,m-1)))
                
            return ans
        return recurse(0,m)
'''

#attempt2: WA because iterated only till some terrible limit
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if n == m:
            return max(nums)
        sums = [0]*n
        sums[0] = nums[0]
        for i in range(1,n):
            sums[i] = sums[i-1] + nums[i]
        if m==1 :
            return sums[-1]
        m -= 1
        @lru_cache(None)
        def recurse(index,m):#at index how many cuts are remaining
            if m==0:
                return sums[-1] - (sums[index-1] if index>=0 else 0)
            if n-1-index+1<m+1:
                return -float('inf')
            if n-1-index+1 == m+1:
                return max(nums[index:])
            ans = float('inf')
            tosubtract = sums[index-1] if index>0 else 0
            for i in range(index,n-1-index+1):
                ans = min(ans,max(sums[i]-tosubtract,recurse(i+1,m-1)))
            return ans
        return recurse(0,m)
'''

#aattempt1: WA had to return sums[-1]  instead of nums[-1]
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if n == m:
            return max(nums)
        sums = [0]*n
        sums[0] = nums[0]
        for i in range(1,n):
            sums[i] = sums[i-1] + nums[i]
        if m==1 :
            return nums[-1]
        m -= 1
        @lru_cache(None)
        def recurse(index,m):#at index how many cuts are remaining
            if m==0:
                return sums[-1] - (sums[index-1] if index>=0 else 0)
            if n-1-index+1<m+1:
                return -float('inf')
            if n-1-index+1 == m+1:
                return max(nums[index:])
            ans = float('inf')
            tosubtract = sums[index-1] if index>0 else 0
            for i in range(index,n-1-index+1):
                ans = min(ans,max(sums[i]-tosubtract,recurse(i+1,m-1)))
            return ans
        return recurse(0,m)
            
        
'''
