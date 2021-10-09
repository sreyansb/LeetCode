#attempt7: Attempt3 improved with LRU caching for triechecker
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            k=trie
            for character in word:
                if character not in k:
                    k[character]={}
                k=k[character]
            k["#"]=1
        ans=[[]]
        @lru_cache(None)
        def triechecker(prefix):
            k=trie
            for i in prefix:
                if i not in k:
                    return False
                k=k[i]
            if "#" in k:
                ans[0].append(prefix)
            return True
    
        m,n=len(board),len(board[0])
        def finder(currow,curcol,curword):
            k=triechecker(curword+board[currow][curcol])
            if k:
                nw=curword+board[currow][curcol]
                val,board[currow][curcol]=board[currow][curcol]," "
                if currow+1<m:
                    finder(currow+1,curcol,nw)
                if currow-1>=0:
                    finder(currow-1,curcol,nw)
                if curcol+1<n:
                    finder(currow,curcol+1,nw)
                if curcol-1>=0:
                    finder(currow,curcol-1,nw)
                board[currow][curcol]=val
        for i in range(m):
            for j in range(n):
                finder(i,j,"")
        return ans[0]

#attempt6: AC
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            k=trie
            for character in word:
                if character not in k:
                    k[character]={}
                k=k[character]
            k["#"]=1
        ans=[set()]
        @lru_cache(None)
        def triechecker(prefix):
            k=trie
            for i in prefix:
                if i not in k:
                    return False
                k=k[i]
            #print(prefix)
            if "#" in k:
                ans[0].add(prefix)
            return True
        m,n=len(board),len(board[0])
        
        def finder(currow,curcol,curword,pr,pc):
            k=triechecker(curword+board[currow][curcol])
            if k:
                nw=curword+board[currow][curcol]
                val,board[currow][curcol]=board[currow][curcol]," "
                if currow+1<m:
                    finder(currow+1,curcol,nw,pr,pc)
                if currow-1>=0:
                    finder(currow-1,curcol,nw,pr,pc)
                if curcol+1<n:
                    finder(currow,curcol+1,nw,pr,pc)
                if curcol-1>=0:
                    finder(currow,curcol-1,nw,pr,pc)
                board[currow][curcol]=val
        
        for i in range(m):
            for j in range(n):
                finder(i,j,"",i,j)
        return list(ans[0])

#attemp5: WA : I tried different stuffs
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            k=trie
            for character in word:
                if character not in k:
                    k[character]={}
                k=k[character]
            k["#"]=1
        ans=[set()]
        @lru_cache(None)
        def triechecker(prefix):
            k=trie
            for i in prefix:
                if i not in k:
                    return False
                k=k[i]
            #print(prefix)
            if "#" in k:
                ans[0].add(prefix)
            return True
        m,n=len(board),len(board[0])
        @lru_cache(None)
        def finder(currow,curcol,curword,pr,pc):
            k=triechecker(curword+board[currow][curcol])
            if k:
                nw=curword+board[currow][curcol]
                val,board[currow][curcol]=board[currow][curcol]," "
                if currow+1<m:
                    finder(currow+1,curcol,nw,pr,pc)
                if currow-1>=0:
                    finder(currow-1,curcol,nw,pr,pc)
                if curcol+1<n:
                    finder(currow,curcol+1,nw,pr,pc)
                if curcol-1>=0:
                    finder(currow,curcol-1,nw,pr,pc)
                board[currow][curcol]=val
        for i in range(m):
            for j in range(n):
                finder(i,j,"",i,j)
        return list(ans[0])
'''

#attempt4:WA: LRU cache should've been only for triechecker
#and not for finder because same position with currow,curcol and curword
#can occur again but with different parent
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            k=trie
            for character in word:
                if character not in k:
                    k[character]={}
                k=k[character]
            k["#"]=1
        ans=[set()]
        def triechecker(prefix):
            k=trie
            for i in prefix:
                if i not in k:
                    return False
                k=k[i]
            if "#" in k:
                ans[0].add(prefix)
            return True
        m,n=len(board),len(board[0])
        @lru_cache(None)
        def finder(currow,curcol,curword):
            k=triechecker(curword+board[currow][curcol])
            if k:
                nw=curword+board[currow][curcol]
                val,board[currow][curcol]=board[currow][curcol]," "
                if currow+1<m:
                    finder(currow+1,curcol,nw)
                if currow-1>=0:
                    finder(currow-1,curcol,nw)
                if curcol+1<n:
                    finder(currow,curcol+1,nw)
                if curcol-1>=0:
                    finder(currow,curcol-1,nw)
                board[currow][curcol]=val
        for i in range(m):
            for j in range(n):
                finder(i,j,"")
        return list(ans[0])
'''

#attempt3: TLE: the answer that was expected in the first attempt
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            k=trie
            for character in word:
                if character not in k:
                    k[character]={}
                k=k[character]
            k["#"]=1
        ans=[set()]
        def triechecker(prefix):
            k=trie
            for i in prefix:
                if i not in k:
                    return False
                k=k[i]
            if "#" in k:
                ans[0].add(prefix)
            return True
        m,n=len(board),len(board[0])
        def finder(currow,curcol,curword):
            k=triechecker(curword+board[currow][curcol])
            if k:
                nw=curword+board[currow][curcol]
                val,board[currow][curcol]=board[currow][curcol]," "
                if currow+1<m:
                    finder(currow+1,curcol,nw)
                if currow-1>=0:
                    finder(currow-1,curcol,nw)
                if curcol+1<n:
                    finder(currow,curcol+1,nw)
                if curcol-1>=0:
                    finder(currow,curcol-1,nw)
                board[currow][curcol]=val
        for i in range(m):
            for j in range(n):
                finder(i,j,"")
        return list(ans[0])
'''

#attempt2:WA: didn't make a visited array or made the previous non allowed
#cells as " "
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            k=trie
            for character in word:
                if character not in k:
                    k[character]={}
                k=k[character]
            k["#"]=1
        ans=[set()]
        def triechecker(prefix):
            k=trie
            for i in prefix:
                if i not in k:
                    return False
                k=k[i]
            if "#" in k:
                ans[0].add(prefix)
            return True
        m,n=len(board),len(board[0])
        def finder(currow,curcol,curword):
            k=triechecker(curword+board[currow][curcol])
            if k:
                if currow+1<m:
                    finder(currow+1,curcol,curword+board[currow][curcol])
                if currow-1>=0:
                    finder(currow-1,curcol,curword+board[currow][curcol])
                if curcol+1<n:
                    finder(currow,curcol+1,curword+board[currow][curcol])
                if curcol-1>=0:
                    finder(currow,curcol-1,curword+board[currow][curcol])
        for i in range(m):
            for j in range(n):
                finder(i,j,"")
        return list(ans[0])
'''


#attempt1: WA: forgot to make ans[0] a set
#should have given an idea that we need to DPISE triechecker
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            k=trie
            for character in word:
                if character not in k:
                    k[character]={}
                k=k[character]
            k["#"]=1
        ans=[[]]
        def triechecker(prefix):
            k=trie
            for i in prefix:
                if i not in k:
                    return False
                k=k[i]
            if "#" in k:
                ans[0].append(prefix)
            return True
        m,n=len(board),len(board[0])
        def finder(currow,curcol,curword):
            k=triechecker(curword+board[currow][curcol])
            if k:
                if currow+1<m:
                    finder(currow+1,curcol,curword+board[currow][curcol])
                if currow-1>=0:
                    finder(currow-1,curcol,curword+board[currow][curcol])
                if curcol+1<n:
                    finder(currow,curcol+1,curword+board[currow][curcol])
                if curcol-1>=0:
                    finder(currow,curcol-1,curword+board[currow][curcol])
        for i in range(m):
            for j in range(n):
                finder(i,j,"")
        return ans[0]
'''