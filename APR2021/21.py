#attempt1:
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        k=float('inf')
        dpt=[[k for i in range(n)] for j in range(n)]
        ans=[k]
        def check(row,index):
            if row==n:
                return 0
            if dpt[row][index]!=k:
                return dpt[row][index]
            dpt[row][index]=triangle[row][index]+min(check(row+1,index),check(row+1,index+1))
            return dpt[row][index]
        return check(0,0)
                
            
            
            
        
