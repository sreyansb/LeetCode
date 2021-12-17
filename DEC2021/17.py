#attempt1: 4006 ms and 15MB - 99.96
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for col in range(n):
            matrix[0][col] = int(matrix[0][col])
        for row in range(1,m):
            for col in range(n):
                matrix[row][col] = int(matrix[row][col])+matrix[row-1][col]
        #print(matrix)
        maxans = 0
        for row1 in range(m):
            for row2 in range(row1,m):
                reqd = (row2-row1+1)
                prodreqd = reqd*reqd
                runningsum = 0
                sumexcludingcol = {}
                for col in range(n):
                    sumexcludingcol[col] = runningsum
                    runningsum += matrix[row2][col] -(matrix[row1-1][col] if row1>0 else 0)
                    if col+1-reqd >=0 and prodreqd == runningsum-sumexcludingcol[col+1-reqd]:
                        maxans = max(maxans,prodreqd)
                #print(row1,row2,sumexcludingcol,runningsum,reqd,prodreqd)
        return maxans
