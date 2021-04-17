#attempt2: TOOK HELP :
#For all such questions where the answer can lead to dead lock between adjacent
#stuff, please do a top-down(left to right) followed by bottom-up (right to left)
#iterations. In the first iterations all the data required for a cell is
#present at its top and left side. In the 2nd iteration, it depends on below
#and right cells thereby we get minimum from all sides.
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        newmatrix=[[float('inf') for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    newmatrix[i][j]=0
                else:
                    if i>0:
                        newmatrix[i][j]=min(newmatrix[i][j],newmatrix[i-1][j]+1)
                    if j>0:
                        newmatrix[i][j]=min(newmatrix[i][j],newmatrix[i][j-1]+1)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j]==0:
                    newmatrix[i][j]=0
                else:
                    if i<m-1:
                        newmatrix[i][j]=min(newmatrix[i][j],newmatrix[i+1][j]+1)
                    if j<n-1:
                        newmatrix[i][j]=min(newmatrix[i][j],newmatrix[i][j+1]+1)
        return newmatrix
        

#attempt1: Wasted TLE method: It results in deaadlock between 2 adjacent matrices
'''
class Solution:
    def updateMatrix(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        newmatrix=[[-1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                newmatrix[i][j]=0 if matrix[i][j]==0 else -1
        print(newmatrix)
        def dfs(i,j):
            print(i,j)
            if i<0 or j<0 or i>=m or j>=n:
                return float('inf')
            if newmatrix[i][j]!=-1:
                return newmatrix[i][j]
            ans=float('inf')
            if i>0:
                if newmatrix[i-1][j]!=-1:
                    ans=min(ans,newmatrix[i-1][j])
            if i<n-1:
                if newmatrix[i+1][j]!=-1:
                    ans=min(ans,dfs(i+1,j))
            if j>0:
                if newmatrix[i][j-1]!=-1:
                    ans=min(ans,dfs(i,j-1))
            
            newmatrix[i][j]=1+min(dfs(i-1,j),dfs(i+1,j),dfs(i,j-1),dfs(i,j+1))
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    dfs(i,j)
        
        return newmatrix
obj=Solution()
print(obj.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
'''
            
        
