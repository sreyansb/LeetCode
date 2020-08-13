class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            if A[i][0]==0:
                for j in range(len(A[i])):
                    A[i][j]^=1
        for i in range(1,len(A[0])):
            nozeros=0
            noones=0
            for j in range(len(A)):
                nozeros+=1 if A[j][i]==0 else 0
                noones+=A[j][i]
            if nozeros>noones:
                for j in range(len(A)):
                    A[j][i]^=1
        sum=0
        for i in A:
            s="".join([str(j) for j in i])
            sum+=int(s,2)
        return sum
                
                
