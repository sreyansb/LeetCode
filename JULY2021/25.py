#attempt1:
from math import ceil,log2
from functools import lru_cache
class Solution:
    def findIntegers(self, n: int) -> int:
        totalb=ceil(log2(n+1))
        k=bin(n)[2:]
        s="0"*(totalb-len(k))+k
        @lru_cache(None)
        def dp(b,parent,tight):
            if b==totalb:
                if parent==0:
                    if tight:
                        if s[b-1]=='1':
                            return 2
                        else:
                            return 1
                    return 2
                else:
                    return 1
            if parent==0:
                if tight:
                    if s[b-1]=='1':
                        return dp(b+1,0,0)+dp(b+1,1,1)
                    else:
                        return dp(b+1,0,1)
                else:
                    return dp(b+1,0,0)+dp(b+1,1,0)
            else:
                return dp(b+1,0,tight&(s[b-1]=='0'))
        return dp(1,0,1)