#DAMN SLOW
class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        grid=[[1 for i in range(n)] for j in range(n)]
        gridfinal=[[]]
        for i in mines:
            grid[i[0]][i[1]]=0
        if n==1:
            return 1-len(mines)
        if n==2:
            if len(mines)==4:
                return 0
            else:
                return 1
        number=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    k=1
                    while(j+k<n and j-k>-1 and i+k<n and i-k>-1 and grid[i][j+k] and grid[i][j-k] and grid[i+k][j] and grid[i-k][j]):
                            k+=1
                    number=max(k,number)
                    #print(i,j,number)
        return number

obj=Solution()
print(obj.orderOfLargestPlusSign(5,[[4,2]]))
            
        
