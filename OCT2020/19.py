#attempt1: 91%
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        mini=float('inf')
        n=len(A)
        for i in range(1,7):
            noswaps=0
            j=0
            while(j<n):
                if A[j]==i:
                    j+=1
                    continue
                if B[j]==i:
                    j+=1
                    noswaps+=1
                    continue
                break
            if j==n:
                mini=min(mini,noswaps)
        for i in range(1,7):
            noswaps=0
            j=0
            while(j<n):
                if B[j]==i:
                    j+=1
                    continue
                if A[j]==i:
                    j+=1
                    noswaps+=1
                    continue
                break
            if j==n:
                mini=min(mini,noswaps)
        if mini==float('inf'):
            return -1
        else:
            return mini
        
            
            
        
