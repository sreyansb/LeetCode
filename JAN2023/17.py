#attempt3: Copied past attempt
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n=len(s)
        @lru_cache(None)
        def recurse(index,parent):
            if index>=n:
                return 0
            
            if parent==0:
                return min(recurse(index+1,int(s[index])),1+recurse(index+1,int(s[index])^1))
            else:
                return recurse(index+1,1) + (1 if s[index]=='0' else 0)
            
        return min(recurse(0,0),recurse(0,1))
                
                    
            
        
