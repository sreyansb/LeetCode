#attempt1: TOOK HELP : Idea is very difficult. Very difficult to observe
class Solution:
    def numTilings(self, n: int) -> int:
        f = [1 for i in range(max(4,n+1))]
        f[0] = 0
        f[1] = 1
        f[2] = 2
        f[3] = 5
        for i in range(4,n+1):
            f[i] = 2*f[i-1] + f[i-3]#asaks
        return f[n]%1000000007
            
                
        
                
        
