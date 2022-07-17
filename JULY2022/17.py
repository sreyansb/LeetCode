#attempt3: TOOK HELP decided to go with DP table but couldn't think of
#i-n_row waala subtrahend
from bisect import bisect_left
from sortedcontainers import SortedList
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if k == 0:
            return 1
        prevrow = [1]*(k+1)  
        for n_row in range(2,n+1):
            newrow = [0] * (k+1)
            newrow[0] = 1
            for i in range(1,k+1):
                newrow[i] = prevrow[i] - (0 if i-n_row<0 else prevrow[i-n_row])
                newrow[i] += newrow[i-1]
            prevrow = newrow
        
        if len(prevrow) <= k:
                return 0
        return (prevrow[k]-prevrow[k-1])%(1000000007)
                

#attempt2: TLE just improved for k==0 case
'''
from bisect import bisect_left
from sortedcontainers import SortedList
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 1000000007
        all_elements = set(range(1,n+1))
        if k == 0:
            return 1
        @lru_cache(None)
        def findans(k,seen):
            if k == 0 and len(seen) == n:
                return 1
            ans = 0
            seen = SortedList(seen)
            for ele in all_elements-set(seen):
                number_of_elements_smaller = seen.bisect_left(ele)
                if k-number_of_elements_smaller >= 0:
                    seen.add(ele)
                    ans += findans(k-number_of_elements_smaller,tuple(seen))
                    seen.remove(ele)
            return ans%mod
        return findans(k,tuple(SortedList([])))
'''

#attemp1: TLE supposedly so!
'''
from bisect import bisect_left
from sortedcontainers import SortedList
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 1000000007
        all_elements = set(range(1,n+1))
        @lru_cache(None)
        def findans(k,seen):
            if k == 0 and len(seen) == n:
                return 1
            ans = 0
            seen = SortedList(seen)
            for ele in all_elements-set(seen):
                number_of_elements_smaller = seen.bisect_left(ele)
                if k-number_of_elements_smaller >= 0:
                    seen.add(ele)
                    ans += findans(k-number_of_elements_smaller,tuple(seen))
                    seen.remove(ele)
            return ans%mod
        return findans(k,tuple(SortedList([])))
'''
