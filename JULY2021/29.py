#attempt2: TOOK CLUE about 2 pass algo
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        newarr=[[float('inf') for i in range(n)] for j in range(m)]
        zeroes=[]
        ones=[]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    newarr[i][j]=0
                else:
                    if i-1>-1:
                        newarr[i][j]=min(newarr[i][j],newarr[i-1][j]+1)
                    if j-1>=0:
                        newarr[i][j]=min(newarr[i][j],newarr[i][j-1]+1)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j]==0:
                    newarr[i][j]=0
                else:
                    if i+1<m:
                        newarr[i][j]=min(newarr[i][j],newarr[i+1][j]+1)
                    if j+1<n:
                        newarr[i][j]=min(newarr[i][j],newarr[i][j+1]+1)
        return newarr

#attempt1: WA because number of 1's == k*m*n and number of 0's == (1-k)*m*n
#therefore the loop will be m*n*n*m
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        newarr=[[-1 for i in range(n)] for j in range(m)]
        zeroes=[]
        ones=[]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    newarr[i][j]=0
                    zeroes.append((i,j))
                else:
                    newarr[i][j]=float('inf')
                    ones.append((i,j))
        for row,col in ones:
            for row1,col1 in zeroes:
                newarr[row][col]=min(abs(row1-row)+abs(col1-col),newarr[row][col])
        return newarr
        
'''