#attempt2: 15000 ms TOOK HELP didn't remember this idea
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+[i for i in nums if i>0]+[1]
        @lru_cache(None)
        def dp(lindex,rindex):
            if lindex+1==rindex:
                return 0
            return max([dp(lindex,i)+nums[lindex]*nums[i]*nums[rindex]+dp(i,rindex) for i in range(lindex+1,rindex)])
        return dp(0,len(nums)-1)

#attempt1: WA because of wrong idea and implementation
'''
from heapq import heapify,heappush,heappop
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        newarr = [(-nums[i],i) for i in range(n)]
        heapify(newarr)
        ans = 0
        while(n):
            high,highindex = newarr[0]
            lval,rval = 1,1
            lindex,rindex = -1,-1
            
            if highindex>0:
                lval = nums[highindex-1]
                lindex = highindex-1
            if highindex < n-1:
                rval = nums[highindex+1]
                rindex = highindex+1
            
            print(n,high,lval,rval)
            ans += -high*lval*rval
            
            if lindex == -1:
                if rindex == -1:
                    nums.pop(highindex)
                else:
                    nums.pop(rindex)
            elif rindex == -1:
                if lindex == -1:
                    nums.pop(highindex)
                else:
                    nums.pop(lindex)
            else:
                if min(lval,rval) == lval:
                    nums.pop(lindex)
                else:
                    nums.pop(rindex)
                    
            n -= 1
            newarr = [(-nums[i],i) for i in range(n)]
            heapify(newarr)
        return ans
'''
