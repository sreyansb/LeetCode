#attempt1:
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        lefi=rigi=float('inf')
        n=len(s)
        leftd=[lefi]*n
        rightd=[lefi]*n
        for i in range(n):
            if s[i]==c:
                lefi=0
            leftd[i]=lefi
            lefi+=1
        for i in range(n-1,-1,-1):
            if s[i]==c:
                rigi=0
            rightd[i]=rigi
            rigi+=1
        return [min(leftd[i],rightd[i]) for i in range(n)]
        
        
