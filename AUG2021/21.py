#attempt1: Remember to make board[r][c]="." in recurse
#because check is based on that
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        empty=[]
        rows={}
        cols={}
        for r in range(9):
            rows[r]=[]
            cols[r]=[]
        
        def check(startr,startc):
            visited=set()
            for r in range(startr,startr+3):
                for c in range(startc,startc+3):
                    if board[r][c]!=".":
                        if board[r][c] in visited:
                            return False
                        visited.add(board[r][c])
            return True
        ans=[0]
            
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    empty.append((r,c))
                else:
                    board[r][c]=int(board[r][c])
                    rows[r].append(board[r][c])
                    cols[c].append(board[r][c])
        n=len(empty)
        
        def recurse(index):
            
            if index>=n:
                ans[0]=board.copy()
                return
            if ans[0]:
                return
            r,c=empty[index]
            #print(board,r,c)
            for i in range(1,10):
                board[r][c]=i
                if board[r][c] not in rows[r] and board[r][c] not in cols[c] and check((r//3)*3,(c//3)*3):
                    rows[r].append(board[r][c])
                    cols[c].append(board[r][c])
                    recurse(index+1)
                    if ans[0]:
                        return
                    else:
                        rows[r].remove(board[r][c])
                        cols[c].remove(board[r][c])
                board[r][c]="."
        
        recurse(0)
        #print(ans[0])
        for r in range(9):
            for c in range(9):
                board[r][c]=str(ans[0][r][c])
        
        
                
        