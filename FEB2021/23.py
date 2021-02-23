#attempt2:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        row=0
        limit=n-1
        col1=0
        while(row<m):
            #print(row,limit)
            col1=0
            while(col1<=limit):
                #print(col1,limit,)
                mid=(col1+limit)//2
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid]>target:
                    limit=mid-1
                else:
                    col1=mid+1
            row+=1
        return False

#attempt1: mlogn approach
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        row=0
        col1=0
        col2=n-1
        def binsearch(i):
            low=0
            end=n-1
            while(low<=end):
                mid=(low+end)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]<target:
                    low=mid+1
                else:
                    end=mid-1
            return False
        while(row<m):
            if binsearch(row):
                return True
            row+=1
        return False
'''
