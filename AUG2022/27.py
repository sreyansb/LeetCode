#attempt1:
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rowlen = len(matrix)
        collen = len(matrix[0])
        for row in range(rowlen):
            for col in range(1,collen):
                matrix[row][col] += matrix[row][col-1]
        maxans = -float('inf')
        for col1 in range(collen):
            for col2 in range(col1,collen):
                sumswehaveseen = SortedList([0])
                lenoflist = 1
                currentsum = 0
                for row in range(rowlen):
                    currentsum += matrix[row][col2] - (matrix[row][col1-1] if col1>0 else 0)
                    posinlist = sumswehaveseen.bisect_left(currentsum - k)
                    if posinlist != lenoflist:
                        maxans = max(maxans,currentsum-sumswehaveseen[posinlist])
                    sumswehaveseen.add(currentsum)
                    lenoflist += 1
        return maxans
