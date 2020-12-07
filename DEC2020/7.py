#attempt1:
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def fillrow(row,startno,direction):
            #print(row)
            if direction:#1 means that fill from left to right
                for i in range(n):
                    if ans[row][i]==-1:
                        ans[row][i]=startno[0]
                        startno[0]+=1
                    
            else:
                for i in range(n-1,-1,-1):
                    if ans[row][i]==-1:
                        ans[row][i]=startno[0]
                        startno[0]+=1
        def fillcol(col,startno,direction):
            #print(col)
            if direction:#1 for up to down
                for i in range(n):
                    if ans[i][col]==-1:
                        ans[i][col]=startno[0]
                        startno[0]+=1
                    
            else:
                for i in range(n-1,-1,-1):
                    if ans[i][col]==-1:
                        ans[i][col]=startno[0]
                        startno[0]+=1  
                    
        ans=[[-1 for i in range(n)] for j in range(n)]
        startno=[1]
        colorrow=1#1 for row
        rdir,curro=1,0
        cdir,curco=1,n-1
        while(startno[0]<n*n+1):
            #print("here",startno,curro,curco)
            if colorrow:
                if rdir:
                    fillrow(curro,startno,rdir)
                    rdir^=1
                    curro=n-1-curro
                else:
                    fillrow(curro,startno,rdir)
                    rdir^=1
                    curro=n-curro
            else:
                if cdir:
                    fillcol(curco,startno,cdir)
                    cdir^=1
                    curco=n-1-curco
                else:
                    fillcol(curco,startno,cdir)
                    cdir^=1
                    curco=n-1-(curco+1)
            colorrow^=1
        return ans
            
        
        
