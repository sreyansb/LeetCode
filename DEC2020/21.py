

#attempt1:WA -> wrong hypothesis
'''
class Solution:
    def smallestRangeII(self, A: List[int], k: int) -> int:
        n=len(A)
        if n==1:
            return 0
        A.sort()
        maxie1=A[-1]
        maxie2=A[-2]
        maxi=float('inf')
        maxi=min(abs((maxie1-k)-(maxie2-k)),maxi)
        maxi=min(abs((maxie1-k)-(maxie2+k)),maxi)
        maxi=min(abs((maxie1+k)-(maxie2-k)),maxi)
        maxi=min(abs((maxie1+k)-(maxie2+k)),maxi)
        return maxi
        
'''
