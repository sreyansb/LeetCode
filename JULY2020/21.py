#Could not implement properly. Saw some hints
def check(board,rowi,coli,rows,columns,word,count):
    if count==len(word):
        return True
    if rowi<0 or rowi>rows or coli<0 or coli>len(board[rowi])-1 or board[rowi][coli]!=word[count] :
        return False
    
    k=board[rowi][coli]
    board[rowi][coli]=" "
    temp=check(board,rowi+1,coli,rows,0,word,count+1) or \
          check(board,rowi-1,coli,rows,0,word,count+1) or \
          check(board,rowi,coli+1,rows,columns,word,count+1) or \
          check(board,rowi,coli-1,rows,columns,word,count+1)
    if temp:
        return True
    board[rowi][coli]=k   
    
    
class Solution:
    def exist(self, board, word):
        rows=len(board)-1
        for i in range(rows+1):
            for j in range(len(board[i])):
                if board[i][j]==word[0] and check(board,i,j,rows,0,word,0):
                    return True
        return False

obj=Solution()
board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
print(obj.exist(board,"ABCCED"))
