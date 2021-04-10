#attempt2: Dont need to add 1 to maxl[0] at last bcoz initial value=0
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxl=[1]
        m=len(matrix)
        n=len(matrix[0])
        dpt=[[0 for i in range(n)] for j in range(m)]
        def check(x,y):
            if x>=m or y>=n:
                return 0
            if dpt[x][y]!=0:
                return dpt[x][y]
            if x>0 and matrix[x-1][y]>matrix[x][y]:
                #print("here1")
                dpt[x][y]=max(dpt[x][y],1+check(x-1,y))
            if y>0 and matrix[x][y-1]>matrix[x][y]:
                #print("here2")
                dpt[x][y]=max(dpt[x][y],1+check(x,y-1))
            if y<n-1 and matrix[x][y+1]>matrix[x][y]:
                #print("here3")
                dpt[x][y]=max(dpt[x][y],1+check(x,y+1))
            if x<m-1 and matrix[x+1][y]>matrix[x][y]:
                #print("here4")
                dpt[x][y]=max(dpt[x][y],1+check(x+1,y))
            maxl[0]=max(maxl[0],dpt[x][y]+1)
            return dpt[x][y]
        for i in range(m):
            for j in range(n):
                check(i,j)
        return maxl[0]
        
#attempt1:
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxl=[0]
        m=len(matrix)
        n=len(matrix[0])
        dpt=[[-1 for i in range(n)] for j in range(m)]
        def check(x,y):
            if x>=m or y>=n:
                return 0
            if dpt[x][y]!=-1:
                return dpt[x][y]
            if x>0 and matrix[x-1][y]>matrix[x][y]:
                #print("here1")
                dpt[x][y]=max(dpt[x][y],1+check(x-1,y))
            if y>0 and matrix[x][y-1]>matrix[x][y]:
                #print("here2")
                dpt[x][y]=max(dpt[x][y],1+check(x,y-1))
            if y<n-1 and matrix[x][y+1]>matrix[x][y]:
                #print("here3")
                dpt[x][y]=max(dpt[x][y],1+check(x,y+1))
            if x<m-1 and matrix[x+1][y]>matrix[x][y]:
                #print("here4")
                dpt[x][y]=max(dpt[x][y],1+check(x+1,y))
            maxl[0]=max(maxl[0],dpt[x][y]+1)
            return dpt[x][y]
        for i in range(m):
            for j in range(n):
                check(i,j)
        return maxl[0]+1
'''
