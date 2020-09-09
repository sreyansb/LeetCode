import numpy as np
import time
class Solution:
    def solveSudoku(self, board):
        empty=[]
        
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    empty.append((i,j))
        
        def checkrow(i,row):
            i=str(i)
            for col in range(9) :
                if board[row][col]==i:
                    return False
            return True
        
        def checkcol(i,col):
            i=str(i)
            for row in range(9) :
                if board[row][col]==i:
                    return False
            return True
        
        def check3x3(val,mainr,mainc):
            val=str(val)
            for row in range(mainr,mainr+3):
                for col in range(mainc,mainc+3):
                    if board[row][col]==val:
                        return False
            return True
        
        def putvalue(index):
            row=empty[index][0]
            col=empty[index][1]
            if board[row][col]=="." or board[row][col]=="10":
                value=0
            else:
                value=int(board[row][col])
            for i in range(value+1,10):
                if checkrow(i,row):
                    if checkcol(i,col):
                        if check3x3(i,3*(row//3),3*(col//3)):
                            board[row][col]=str(i)
                            break
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            if board[row][col]==str(value):
                board[row][col]="10"
        
        index=0
        while(index<len(empty)):
            putvalue(index)
            #print(index,board[empty[index][0]][empty[index][1]])
            if board[empty[index][0]][empty[index][1]]=="." or board[empty[index][0]][empty[index][1]]=="10":
                index-=1
            else:
                index+=1    
            print(np.array(board))
            print()
            time.sleep(0.1)
              
obj=Solution()
obj.solveSudoku([["5","3",".",".","7",".",".",".","."],\
                 ["6",".",".","1","9","5",".",".","."],\
                 [".","9","8",".",".",".",".","6","."],\
                 ["8",".",".",".","6",".",".",".","3"],\
                 ["4",".",".","8",".","3",".",".","1"],\
                 ["7",".",".",".","2",".",".",".","6"],\
                 [".","6",".",".",".",".","2","8","."],\
                 [".",".",".","4","1","9",".",".","5"],\
                 [".",".",".",".","8",".",".","7","9"]])
