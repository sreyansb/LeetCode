#attempt1:
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @lru_cache(None)
        def findSol(index):
            if index >= n-1:
                return 0 if (index == n-1 and s[index] == '0') else 1
            if s[index] == '0':
                return 0
            if s[index] > '2':
                return findSol(index+1)
            elif s[index+1] == '0':
                return findSol(index+2)
            elif s[index] == '1' or (s[index] == '2' and s[index+1] < '7'): 
                return findSol(index+1) + findSol(index+2)
            else:
                return findSol(index+1)
        return findSol(0)
                    
                
            
