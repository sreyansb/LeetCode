#attempt3: We need just one index as it is always till the end of string
from functools import lru_cache
class Solution:
    def minCut(self, s: str) -> int:
        end=len(s)-1
        @lru_cache(None)
        def recurse(start):#start and end are included in the string
            if start>=end:
                return 0
            if s[start:]==s[start:][::-1]:
                return 0
            ans=float('inf')
            for i in range(start,end):
                if s[start:i+1]==s[start:i+1][::-1]:
                    ans=min(ans,1+recurse(i+1))
            return ans
        return recurse(0)

#attempt2: WITHOUT LRU_CACHE
'''
from functools import lru_cache
class Solution:
    def minCut(self, s: str) -> int:
        dpt=[[-1 for i in range(len(s))]for j in range(len(s))]
        def recurse(start,end):#start and end are included in the string
            if start>=end:
                return 0
            if s[start:end+1]==s[start:end+1][::-1]:
                return 0
            if dpt[start][end]==-1:
                ans=float('inf')
                for i in range(start,end):
                    if s[start:i+1]==s[start:i+1][::-1]:
                        ans=min(ans,1+recurse(i+1,end))
                dpt[start][end]=ans
            return dpt[start][end]
        return recurse(0,len(s)-1)
'''


#attempt1: AC
'''
from functools import lru_cache
class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(None)
        def recurse(start,end):#start and end are included in the string
            if start>=end:
                return 0
            if s[start:end+1]==s[start:end+1][::-1]:
                return 0
            ans=float('inf')
            for i in range(start,end):
                if s[start:i+1]==s[start:i+1][::-1]:
                    ans=min(ans,1+recurse(i+1,end))
            return ans
        return recurse(0,len(s)-1)
'''