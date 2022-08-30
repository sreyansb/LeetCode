#attempt1:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rowl = len(matrix)
        for row in range(rowl):
            for col in range(row):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
        for row in range(rowl):
            start,end = 0,rowl-1
            while(start <= end):
                matrix[row][start],matrix[row][end] = matrix[row][end],matrix[row][start]
                start += 1
                end -= 1
        return
                
            
                
        
