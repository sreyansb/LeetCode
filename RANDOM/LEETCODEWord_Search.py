#attempt4: Instead of having visited: I just made board[r][c]=" ", to prevent
#further checking of same indices
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        leng=len(word)
        ans=[False]
        def finding(r,c,curword,wordindex):
            if ans[0] or not(0<=r<m and 0<=c<n) or wordindex>=leng:
                return
            curword+=board[r][c]
            if curword==word:
                ans[0]=True
                return
            if word[wordindex]!=curword[wordindex]:
                return
            k,board[r][c]=board[r][c]," "
            for rn,cn in [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]:
                finding(rn,cn,curword,wordindex+1)
            board[r][c]=k
        for r in range(m):
            for c in range(n):
                if board[r][c]==word[0] and not(ans[0]):
                    finding(r,c,"",0)
        return ans[0]

#attempt3: AC
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        leng=len(word)
        ans=[False]
        def finding(r,c,visited,curword,wordindex):
            if ans[0] or not(0<=r<m and 0<=c<n) or wordindex>=leng:
                return
            curword+=board[r][c]
            if curword==word:
                ans[0]=True
                return
            if word[wordindex]!=curword[wordindex]:
                return
            for rn,cn in [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]:
                if (rn,cn) not in visited:
                    finding(rn,cn,visited|{(r,c)},curword,wordindex+1)
        for r in range(m):
            for c in range(n):
                if board[r][c]==word[0] and not(ans[0]):
                    finding(r,c,set(),"",0)
        return ans[0]

#attempt2:TLE In the next iteration I prevented more function calls by checking
#visited at the site of call itself
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        ans=[False]
        def finding(r,c,visited,curword,wordindex):
            if ans[0] or not(0<=r<m and 0<=c<n) or (r,c) in visited:
                return
            curword+=board[r][c]
            if curword==word:
                ans[0]=True
                return
            if word[wordindex]!=curword[wordindex]:
                return
            for rn,cn in [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]:
                finding(rn,cn,visited|{(r,c)},curword,wordindex+1)
        for r in range(m):
            for c in range(n):
                if board[r][c]==word[0] and not(ans[0]):
                    finding(r,c,set(),"",0)
        return ans[0]
'''

#attempt1: TLE NExt idea was to check if th character at current index in 
#curword and original word is same
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        ans=[False]
        def finding(r,c,visited,curword):
            #print(r,c,curword,visited)
            if ans[0] or not(0<=r<m and 0<=c<n) or (r,c) in visited:
                return
            curword+=board[r][c]
            if curword==word:
                ans[0]=True
                return
            for rn,cn in [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]:
                finding(rn,cn,visited|{(r,c)},curword)
        for r in range(m):
            for c in range(n):
                if board[r][c]==word[0]:
                    finding(r,c,set(),"")
        return ans[0]
'''