#attempt1:
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(1,cols):
                matrix[row][col] += matrix[row][col-1]
        ans = 0
        for col1 in range(cols):
            for col2 in range(col1,cols):
                di = {0:1}
                currentsum = 0
                for row in range(rows):
                    subtrahend = matrix[row][col1-1] if col1>0 else 0
                    
                    value_to_be_checked = matrix[row][col2] - subtrahend
                    currentsum += value_to_be_checked
                    if currentsum-target in di:
                        ans += di[currentsum-target]
                    
                    if currentsum not in di:
                        di[currentsum] = 0
                    di[currentsum] += 1
        return ans
