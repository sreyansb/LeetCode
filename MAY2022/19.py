#attempt1:
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        dpt = [[0 for i in range(n)]for j in range(m)]
        def calculate_max_distance(row,col):
            if not(0<=row<m) or not(0<=col<n):
                return 0
            if dpt[row][col] != 0:
                return dpt[row][col]
            ans = 1
            for newrow,newcol in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                if not(0<=newrow<m) or not(0<=newcol<n) or matrix[newrow][newcol] <= matrix[row][col]:
                    continue
                ans = max(ans,1+calculate_max_distance(newrow,newcol))
            dpt[row][col] = ans
            return dpt[row][col]
        ans = 1
        for row in range(m):
            for col in range(n):
                if dpt[row][col] == 0:
                    calculate_max_distance(row,col)
        #print(dpt)
        return max([max(row) for row in dpt])
        
        
