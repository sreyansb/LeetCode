#attempt1:
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        @lru_cache(None)
        def findAns(row, col):
            if not(0<=col<n):
                return float('inf')
            if row == n-1:
                return matrix[row][col]
            return matrix[row][col] + min(findAns(row+1, col), findAns(row+1,col+1), findAns(row+1, col-1))
        minAns = float('inf')
        for col in range(n):
            minAns = min(minAns, findAns(0,col))
        return minAns
