#attempt1: We just need to restructure the entire thing into a different array of size r*c
class Solution:
    def matrixReshape(self, matrix: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        if r*c!=m*n:
            return matrix
        ans=[[-1 for i in range(c)]for j in range(r)]
        currow=0
        curcol=0
        for row in range(m):
            for col in range(n):
                if curcol==c:
                    currow+=1
                    curcol=0
                ans[currow][curcol]=matrix[row][col]
                curcol+=1
        return ans
        