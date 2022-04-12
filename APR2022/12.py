#attempt1: While submitting, had many issues like not updating board
#work carefully
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        total_rows = len(board)
        total_cols = len(board[0])
        
        def get_live_cells_count(row,col):
            count = 0
            for newrow in range(row-1,row+2):
                for newcol in range(col-1,col+2):
                    if (0<=newrow<total_rows and 0<=newcol<total_cols) and board[newrow][newcol]:
                        count += 1
            return count-board[row][col]
            
        locations_changed = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                count = get_live_cells_count(row,col)
                if board[row][col]:
                    if count < 2 or count>3:
                        locations_changed[(row,col)] = 0
                else:
                    if count == 3:
                        locations_changed[(row,col)] = 1
        for row,col in locations_changed:
            board[row][col] = locations_changed[(row,col)]
                
        
        
