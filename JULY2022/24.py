#attempt2: TOOK HELp start from left most col and row and move up or right
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = 0
        while(row>=0 and col < len(matrix[0])):
            if matrix[row][col] == target:
                return True
            if target > matrix[row][col]:
                col += 1
            else:
                row -= 1
        return False
                
        
        

#attempt1:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False
        
