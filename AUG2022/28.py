#attempt1:
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        di = {}
        m,n = len(mat),len(mat[0])
        for row in range(m):
            for col in range(n):
                if row-col not in di:
                    di[row-col] = []
                di[row-col].append(mat[row][col])
        for diagdiff in di:
            di[diagdiff].sort(reverse=True)
        for row in range(m):
            for col in range(n):
                mat[row][col] = di[row-col].pop()
        return mat
