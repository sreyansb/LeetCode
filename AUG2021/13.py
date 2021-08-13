#attempt2: Make original 0s as (0,0) where 2nd 0 shows that the zero at that cell
#should be explored. (0,1) shows that that cell shouldn't be explored
#atlast make all such tuples as 0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeror=set()
        zeroc=set()
        m=len(matrix)
        n=len(matrix[0])
        count=0
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0:
                    count=1
                    matrix[row][col]=(0,0)
        if count==0:
            return
        
        def changec(col):
            for row in range(m):
                if matrix[row][col]==(0,0):#already zero tha, dont have to change this
                    continue
                matrix[row][col]=(0,1)
                
        for row in range(len(matrix)):
            flag=0#meaning we havent seen a zero yet
            #i will find the column with zero and then for each row change it to 0,1 stating has been changed
            #or 0,0 if already it was zero
            for col in range(len(matrix[row])):
                if matrix[row][col]==(0,0):
                    flag=1
                    changec(col)
                    matrix[row][col]=(0,1)
            if flag:
                for col in range(len(matrix[row])):
                    matrix[row][col]=(0,1)
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==(0,0) or matrix[row][col]==(0,1):
                    matrix[row][col]=0

#attempt1:What I did find all rows and columns which have zero
#then make all elements in those rows and columns as 0
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeror=set()
        zeroc=set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col]==0:
                    zeror.add(row)
                    zeroc.add(col)
        for row in zeror:
            for col in range(len(matrix[row])):
                matrix[row][col]=0
        for col in zeroc:
            for row in range(len(matrix)):
                matrix[row][col]=0
'''