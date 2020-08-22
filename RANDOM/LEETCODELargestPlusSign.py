class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        grid=[[1 for i in range(n)] for j in range(n)]
        for i in mines:
            grid[i[0]][i[1]]=0
        if n==1:
            return 1-len(mines)
        if n==2:
            if len(mines)==4:
                return 0
            else:
                return 1
        if len(mines)==n*n:
            number=0
        else:
            number=1
        #print(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    #print(i,j,grid[i][j])
                    k=1
                    while(True):
                        if (j+k<n and grid[i][j+k] and j-k>-1 and grid[i][j-k] and i+k<n and grid[i+k][j] and i-k>-1 and grid[i-k][j]):
                            k+=1
                        else:
                            break
                    number=max(k,number)
                    #print(i,j,number)
        return number
            
obj=Solution()
print(obj.orderOfLargestPlusSign(5,[[0,0],[0,3],[1,1],[1,4],[2,3],[3,0],[4,2]]))
