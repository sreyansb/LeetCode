#attempt1: What all places pacific can flow to, what all places atlantic can
#go to. See where both are common
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        if not(m):
            return []
        n=len(matrix[0])
        if not(n):
            return []
        k=-float('inf')
        
        def dfs(x,y,curarr,prev):
            if x>=m or y>=n or x<0 or y<0 or prev>matrix[x][y] or curarr[x][y]:
                return
            curarr[x][y]=1
            dfs(x+1,y,curarr,matrix[x][y])
            dfs(x-1,y,curarr,matrix[x][y])
            dfs(x,y+1,curarr,matrix[x][y])
            dfs(x,y-1,curarr,matrix[x][y])               
            
        atlantic=[[0 for i in range(n)] for j in range(m)]
        pacific=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dfs(i,0,pacific,k)
            dfs(i,n-1,atlantic,k)
        for i in range(n):
            dfs(0,i,pacific,k)
            dfs(m-1,i,atlantic,k)
        ans=[]
        for i in range(m):
            for j in range(n):
                if atlantic[i][j] and pacific[i][j]:
                    ans.append([i,j])
        return ans
