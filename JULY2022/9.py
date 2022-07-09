#attempt4: TOOK HINTS - didn't think of heap with DP
from heapq import heappush, heappop
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        ans = [-float('inf')]*n
        index = n-1
        while(index>=0):
            while(heap and heap[0][1]>index+k):
                heappop(heap)
            ans[index] = nums[index]
            if heap:
                ans[index] += -heap[0][0]
            heappush(heap,(-ans[index],index))
            index -= 1
        return ans[0]

#attempt3: WA : I thought that we should go backwards
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        index = 0
        ans = 0
        while(index < n-1):
            ans += nums[index]
            nextindex = index+1
            maxn = -float('inf')
            maxindex = index
            while(nextindex <= min(index+k,n-1)):
                if nums[nextindex] > 0:
                    maxindex = nextindex
                    break
                if nums[nextindex] > maxn:
                    maxn = nums[nextindex]
                    maxindex = nextindex
                nextindex += 1
            index = maxindex
        index = n-1
        ans1 = 0
        while(index > 0):
            ans1 += nums[index]
            nextindex = index-1
            maxn = -float('inf')
            maxindex = index
            while(nextindex >= max(index-k,0)):
                if nums[nextindex] > 0:
                    maxindex = nextindex
                    break
                if nums[nextindex] > maxn:
                    maxn = nums[nextindex]
                    maxindex = nextindex
                nextindex -= 1
            index = maxindex
        return max(ans+nums[-1],ans1+nums[0])
'''

#attempt2: WA : because we need to look into the future. Not just current answer
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        index = 0
        ans = 0
        while(index < n-1):
            ans += nums[index]
            nextindex = index+1
            maxn = -float('inf')
            maxindex = index
            while(nextindex <= min(index+k,n-1)):
                if nums[nextindex] > 0:
                    maxindex = nextindex
                    break
                if nums[nextindex] > maxn:
                    maxn = nums[nextindex]
                    maxindex = nextindex
                nextindex += 1
            index = maxindex
        return ans+nums[-1]
'''

#attempt1: TLE
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def findsol(index):
            if index >= n:
                return -float('inf')
            if index == n-1:
                return nums[-1]
            ans = -float('inf')
            for nextindex in range(index+1,min(n-1,index+k)+1):
                ans = max(ans,findsol(nextindex))
            return ans+nums[index]
        return findsol(0)
'''
