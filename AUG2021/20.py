#attempt1:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        cols={}
        
        def checksquare(startrow,startcol):
            visited=set()
            for i in range(startrow,startrow+3):
                for j in range(startcol,startcol+3):
                    if board[i][j]!='.':
                        if board[i][j] in visited:
                            #print(startrow,startcol)
                            return False
                        visited.add(board[i][j])
            return True
        
        for startrow in range(0,9,3):
            for startcol in range(0,9,3):
                if not checksquare(startrow,startcol):
                    return False
        
        for row in range(9):
            if row not in rows:
                rows[row]=set()
            for col in range(9):
                if col not in cols:
                    cols[col]=set()
                if board[row][col]==".":
                    continue
                if board[row][col] in rows[row]:
                    #print("row",row,rows[row])
                    return False
                if board[row][col] in cols[col]:
                    #print(col)
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
        return True
                
        
                    
        