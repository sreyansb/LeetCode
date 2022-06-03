#attempt1:
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix),len(matrix[0])
        self.sum_matrix = [[0 for i in range(n)] for j in range(m)]
        for row in range(m):
            prevsum = 0
            for col in range(n):
                self.sum_matrix[row][col] = prevsum + matrix[row][col]
                prevsum = self.sum_matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for row in range(row1,row2+1):
            ans += self.sum_matrix[row][col2] - ( 0 if col1 == 0 else self.sum_matrix[row][col1-1])
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
