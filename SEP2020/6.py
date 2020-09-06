#Attempt1: 60% and 99.62%
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n=len(A)
        maxi=0
        def check(i,j):
            no=0
            for a in range(i,n):
                for b in range(j,n):
                    if A[a-i][b-j] and B[a][b]:
                        no+=1
            return no
        
        def check1(i,j):
            no=0
            for a in range(i,n):
                for b in range(j,n):
                    if B[a-i][b-j] and A[a][b]:
                        no+=1
            return no
        
        for i in range(n):
            for j in range(n):
                maxi=max(maxi,check(i,j),check1(i,j))
        return maxi
            
