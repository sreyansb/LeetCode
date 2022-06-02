#attempt2: 1 was wrong because I was mostly too quick
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        finmatrix = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                finmatrix[j][i]=matrix[i][j]
        return finmatrix
        
