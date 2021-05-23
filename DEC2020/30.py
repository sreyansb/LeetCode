#attempt1:
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        boardc=[i.copy() for i in board]
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                lives=0
                deads=0
                if i-1>-1:
                    if j-1>-1:
                        if board[i-1][j-1]:
                            lives+=1
                        else:
                            deads+=1
                    if j+1<n:
                        if board[i-1][j+1]:
                            lives+=1
                        else:
                            deads+=1
                    lives+=1 if board[i-1][j] else 0
                    deads+=0 if board[i-1][j] else 1
                if i+1<m:
                    if j-1>-1:
                        if board[i+1][j-1]:
                            lives+=1
                        else:
                            deads+=1
                    if j+1<n:
                        if board[i+1][j+1]:
                            lives+=1
                        else:
                            deads+=1
                    lives+=1 if board[i+1][j] else 0
                    deads+=0 if board[i+1][j] else 1
                if j-1>-1:
                        if board[i][j-1]:
                            lives+=1
                        else:
                            deads+=1
                if j+1<n:
                        if board[i][j+1]:
                            lives+=1
                        else:
                            deads+=1
                if board[i][j]:
                    if lives<2:
                        boardc[i][j]=0
                    elif lives<4:
                        boardc[i][j]=1
                    else:
                        boardc[i][j]=0
                else:
                    if lives==3:
                        boardc[i][j]=1
        for i in range(m):
            for j in range(n):
                board[i][j]=boardc[i][j]
                    
                        
                        
        