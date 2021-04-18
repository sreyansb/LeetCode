#attempt1: TOOK HELP: VERY DIFFICULT problem
#first count the number of continuous 1s row wise.
#then go row by row, and between columns: like from column j to k
#For each column in jth loop, you add the number: To mark all from the top
#then between columns is for sideways matrix

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        for i in range(1,len(mat)):
            for j in range(len(mat[i])):
                mat[i][j]=0 if mat[i][j]==0  else mat[i-1][j]+1
        ans=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mini=float('inf')
                for k in range(j,-1,-1):
                    mini=min(mini,mat[i][k])
                    ans+=mini
        return ans
                    

        
