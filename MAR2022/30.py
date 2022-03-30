#attempt1:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(row):
            start = 0
            end = len(row)-1
            while(start<=end):
                mid = (start+end)//2
                if row[mid] == target:
                    return True
                elif target>row[mid]:
                    start = mid+1
                else:
                    end = mid-1
            return False
        for row in matrix:
            if target>row[-1]:
                continue
            elif target<row[0]:
                break
            else:
                return binarysearch(row)
        return False
                
                
        
