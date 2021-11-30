#attempt2: TOOK HELP: get running sum of each row for each column to get max
#continuous 1s for that column.
#then for each row and each column, go back to the starting columns and that is
#the width and height is the minimum from basecol to current col
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not(matrix):
            return 0
        m,n = len(matrix),len(matrix[0])
        maxans = 0
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j] if i-1>=0 else 0
                else:
                    matrix[i][j] = 0
        #print(matrix)
        for baserow in range(m):
            maxhere = 0
            for col in range(n):
                minh = matrix[baserow][col]
                col2 = col
                while(col2 > -1 and matrix[baserow][col2]):
                    minh = min(minh,matrix[baserow][col2])
                    maxhere = max(maxhere,minh*(col-col2+1))
                    #print(maxhere,col2,col,baserow,minh)
                    col2 -= 1
            #print(baserow,maxhere)
            maxans = max(maxans,maxhere)
                                
        return maxans

#attempt1: TLE used a problem technique used before.
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not(matrix):
            return 0
        m,n = len(matrix),len(matrix[0])
        maxans = 0
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    maxans = 1
                if i>0:
                    matrix[i][j] += matrix[i-1][j]
                    
        for r1 in range(m):
            for r2 in range(r1,m):
                di = {0:{-1}}
                cursum = 0
                for c in range(n):
                    cursum += matrix[r2][c]-matrix[r1-1][c] if r1-1>=0 else matrix[r2][c]
                    for prevsum in di:
                        if (cursum-prevsum)%(r2-r1+1) == 0:
                            #print("HERE",cursum,prevsum,r1,r2,c,di[prevsum])
                            if c-((cursum-prevsum)//(r2-r1+1)) in di[prevsum]:
                                maxans = max(maxans,cursum-prevsum)
                    if cursum not in di:
                        di[cursum] = set()
                    di[cursum].add(c)
                                
            
        return maxans
        
'''
