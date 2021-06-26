#attempt3: if * then increment sindex by 1 or pindex by 1 and continue
from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen=len(s)
        plen=len(p)
        @lru_cache(None)
        def check(sindex,pindex):
            if sindex==slen:
                return pindex==plen or set(p[pindex:])=={"*"}
            if pindex==plen:
                return False
            if p[pindex]=='*':
                return check(sindex+1,pindex) or check(sindex,pindex+1)
                    
            elif p[pindex]=='?':
                return check(sindex+1,pindex+1)
            else:
                if s[sindex]==p[pindex]:
                    return check(sindex+1,pindex+1)
                return False
        return check(0,0)

#attempt2 and 1:TLE used regex
"""
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        final=""
        for i,ch in enumerate(p):
            if i==0:
                final=final+ch
            else:
                if p[i]=='*' and p[i-1]=='*':
                    continue
                final=final+ch
        p=final
        p=p.replace("*","[a-z]*")
        p=p.replace("?","[a-z]")
        p="^"+p+"$"
        #print(p)
        return re.match(p,s)
"""