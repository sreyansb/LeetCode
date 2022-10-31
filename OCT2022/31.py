#attempt1:
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n = len(matrix),len(matrix[0])
        diagonalValues = {}
        for rowNumber in range(m):
            for colNumber in range(n):
                if rowNumber-colNumber not in diagonalValues:
                    diagonalValues[rowNumber-colNumber] = set()
                diagonalValues[rowNumber-colNumber].add(matrix[rowNumber][colNumber])
        return False if any([len(diagonalValues[key]) > 1 for key in diagonalValues]) else True
