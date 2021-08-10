#attempt1:Just flip and everything before current index  is proper

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n=len(s)
        @lru_cache(None)
        def recurse(index,parent):
            if index>=n:
                return 0
            
            ans=float('inf')
            if parent==0:
                ans=min(recurse(index+1,int(s[index])),1+recurse(index+1,int(s[index])^1))
            else:
                ans=recurse(index+1,1) if s[index]=='1' else 1+recurse(index+1,1)
            #pt[index,parent]=ans
            return ans
        return min(recurse(0,0),recurse(0,1))
