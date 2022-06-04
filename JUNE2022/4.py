#attempt1:
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []
        
        def createnewboard(visited):
            board = [["." for i in range(n)] for row in range(n)]
            for row,col in visited:
                board[row][col] = 'Q'
            board = ["".join(i) for i in board]
            return board
        
        def findpositions(currentrow,prevcol,blocked,visited):
            
            if currentrow<0:
                return
            if currentrow>=n:
                boards.append(createnewboard(visited))
                return
            is_position_found = False
            for col in range(prevcol+1,n):
                if not(blocked[currentrow][col]):
                    for nextrow in range(n):
                        blocked[nextrow][col] += 1
                        blocked[currentrow][nextrow] += 1
                        #currentrow-col == nextrow-nextcol
                        #nextcol = nextrow-currentrow+col
                        if 0 <= nextrow-currentrow+col < n:
                            blocked[nextrow][nextrow-currentrow+col] += 1
                        if 0 <= currentrow+col-nextrow < n:
                            blocked[nextrow][currentrow+col-nextrow] += 1
                    
                    findpositions(currentrow+1,-1,blocked,visited+[(currentrow,col)])
                    for nextrow in range(n):
                        blocked[nextrow][col] -= 1
                        blocked[currentrow][nextrow] -= 1
                        #currentrow-col == nextrow-nextcol
                        #nextcol = nextrow-currentrow+col
                        if 0 <= nextrow-currentrow+col < n:
                            blocked[nextrow][nextrow-currentrow+col] -= 1
                        if 0 <= currentrow+col-nextrow < n:
                            blocked[nextrow][currentrow+col-nextrow] -= 1                    
        findpositions(0,-1,[[0 for i in range(n)]for i in range(n)],[])
        return boards
