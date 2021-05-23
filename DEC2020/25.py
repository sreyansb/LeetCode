#attempt1: ALong a diagonal sum of rows and columns remains same
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        di={}
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i+j not in di:
                    di[i+j]=[]
                di[i+j].append((i,j))
        descsort=1
        for i in di:
            if descsort:
                di[i].sort(key=lambda x:-x[0])
            else:
                di[i].sort(key=lambda x:x[0])
            descsort^=1
        ans=[]
        for i in di:
            for r,c in di[i]:
                ans.append(matrix[r][c])
        return ans
            
        
            
        
        