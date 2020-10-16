#attempt1: 93% and 50%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not(matrix):
            return False
        rows=len(matrix)
        cols=len(matrix[0])
        if cols==0:
            return False
        index=0
        while(index<rows):
            if target>matrix[index][-1]:
                index+=1
                continue
            if target<matrix[index][0]:
                return False
            if target>=matrix[index][0] and target<=matrix[index][-1]:
                start=0
                end=cols-1
                while(start<=end):
                    mid=(start+end)//2
                    if matrix[index][mid]==target:
                        return True
                    if matrix[index][mid]>target:
                        end=mid-1
                    else:
                        start=mid+1
                return False
        #print("here1")
        return False
            
        
