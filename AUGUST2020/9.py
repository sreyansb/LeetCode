#1st attempt. Thought that I couldn't do it
def helper(grid):
    flag=1
    ans=0
    while(flag):
        flag=0
        copyy=[]
        for i in grid:
            copyy.append(i.copy())#copyy=grid.copy() does not work, if copyy changes then grid was also changing
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    if i-1>-1 and grid[i-1][j]==1:
                        flag=1
                        copyy[i-1][j]=2
                    if j-1>-1 and grid[i][j-1]==1:
                        flag=1
                        copyy[i][j-1]=2
                    if i+1<len(grid) and grid[i+1][j]==1:
                        flag=1
                        copyy[i+1][j]=2
                    if j+1<len(grid[i]) and grid[i][j+1]==1:
                        flag=1
                        copyy[i][j+1]=2
        #print(copyy)
        for i in range(len(copyy)):
            grid[i]=(copyy[i].copy())
        if flag:
            ans+=1
        #print(grid)
    return ans
    
            
class Solution:
    def orangesRotting(self, grid):
        ans=helper(grid)
        #print("g",grid)
        for i in grid:
            for j in i:
                
                if j==1:
                    ans=-1
                    break
        return ans
obj=Solution()
#print(obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(obj.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
