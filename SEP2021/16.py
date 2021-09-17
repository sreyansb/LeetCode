#attempt2: My Attempt
class Solution:
    def spiralOrder(self, matrix):
        m,n=len(matrix),len(matrix[0])
        count=0
        rorc=1
        rdir=1
        cdir=1
        currow=0
        curcol=0
        ans=[]
        while(count<m*n):
            #print(currow,curcol)
            if rorc:#1 -> we are filling a row => column has to be filled
                if (0<=curcol<n) and matrix[currow][curcol]!="*":
                    ans.append(matrix[currow][curcol])
                    matrix[currow][curcol]="*"
                    curcol+=cdir
                    count+=1
                else:
                    cdir*=-1
                    curcol+=cdir
                    rorc^=1
                    currow+=rdir
                    
            else:
                if (0<=currow<m) and matrix[currow][curcol]!="*":
                    ans.append(matrix[currow][curcol])
                    matrix[currow][curcol]="*"
                    currow+=rdir
                    count+=1
                else:
                    rdir*=-1
                    currow+=rdir
                    rorc^=1
                    curcol+=cdir
        return ans
                    
#attempt1:TOOK HELp, no mood to solve
'''
class Solution:
    def spiralOrder(self, matrix):
        n, m = len(matrix[0]), len(matrix)
        x, y, dx, dy = 0, 0, 1, 0
        ans = []
        for _ in range(m*n):
            if not 0 <= x+dx < n or not 0 <= y+dy < m or matrix[y+dy][x+dx] == "*":
                dx, dy = -dy, dx
                
            ans.append(matrix[y][x])
            matrix[y][x] = "*"
            x, y = x + dx, y + dy
        
        return ans
'''