#attempt3: AC: Pending is when len(moves)<9 else DRAW. No need for elaborate stuff
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board=[["" for i in range(3)]for j in range(3)]           
            
        cur=1
        for r,c in moves:
            board[r][c]=cur
            cur^=1
        #to prove if answer exists
        #print(board)
        if board[0][0]!="":
            flag=1
            for r in range(3):
                if board[r][r]!=board[0][0]:
                    flag=0
                    break
            if flag:
                return "A" if board[0][0]==1 else "B"
        if board[0][2]!="":
            flag=1
            for r in range(2,-1,-1):
                if board[2-r][r]!=board[0][2]:
                    flag=0
                    break
            if flag:
                return "A" if board[0][2]==1 else "B"
        for r in range(3):
            if board[r][0]!="":
                if board[r][0]==board[r][1]==board[r][2]:
                    return "A" if board[r][0]==1 else "B"
            if board[0][r]!="":
                if board[0][r]==board[1][r]==board[2][r]:
                    return "A" if board[0][r]==1 else "B"
        #to check for draw or pending
        if len(moves)==9:
            return "Draw"
        
        return "Pending"

#attempt1&2: WA because AI is not supported by LeetCode!
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board=[["" for i in range(3)]for j in range(3)]           
            
        cur=1
        for r,c in moves:
            board[r][c]=cur
            cur^=1
        #to prove if answer exists
        
        if board[0][0]!="":
            flag=1
            for r in range(3):
                if board[r][r]!=board[0][0]:
                    flag=0
                    break
            if flag:
                return "A" if board[0][0]==1 else "B"
        if board[0][2]!="":
            flag=1
            for r in range(2,-1,-1):
                if board[2-r][r]!=board[0][2]:
                    flag=0
                    break
            if flag:
                return "A" if board[0][2]==1 else "B"
        for r in range(3):
            if board[r][0]!="":
                if board[r][0]==board[r][1]==board[r][2]:
                    return "A" if board[r][0]==1 else "B"
            if board[0][r]!="":
                if board[0][r]==board[1][r]==board[2][r]:
                    return "A" if board[0][r]==1 else "B"
        
        #to check for draw or pending
        if len(moves)<=4:
            return "Pending"
        
        for r in range(3):
            a={board[r][0],board[r][1],board[r][2]}
            if not(0 in a and 1 in a) and "" in a:
                return "Pending"
            a={board[0][r],board[1][r],board[2][r]}
            if not(0 in a and 1 in a) and "" in a:
                return "Pending"
        a={board[0][0],board[1][1],board[2][2]}
        if not(0 in a and 1 in a) and "" in a:
                return "Pending"
        a={board[0][2],board[1][1],board[2][0]}
        if not(0 in a and 1 in a) and "" in a:
                return "Pending"
        return "Draw"
'''