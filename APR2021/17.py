#attempt1: TOOK HELP
#prefix 2d sum is used here. Calculate column wise sum
#between 2 rows(r1 and r2) and then apply similarly as 1d sum
#remember it is sumtillhere-target and not other way round
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(1,m):
            for j in range(n):
                matrix[i][j]+=matrix[i-1][j]
        ans=0
        for r1 in range(m):
            for r2 in range(r1,m):
                ps=0
                di={0:1}
                for col in range(n):
                    val=0 if r1==0 else matrix[r1-1][col]
                    ps+=matrix[r2][col]-val
                    if ps-target in di:
                        ans+=di[ps-target]
                    if ps not in di:
                        di[ps]=0
                    di[ps]+=1
        return ans
            
