#attempt1:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        start=0
        end=n-1
        while(start<=end):
            for j in range(n):
                matrix[j][start],matrix[j][end]=matrix[j][end],matrix[j][start]
            start+=1
            end-=1
        
        return matrix
        
        
        
