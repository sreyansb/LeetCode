#attempt5: AC after taking help.
#important to have counter such that you reverse the word for quick termination
#of the dfs
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        
        def dfs(currentRow, currentCol, wordTillHere):
            charHere = board[currentRow][currentCol]
            board[currentRow][currentCol] = " "
            currentWord = wordTillHere+charHere
            if currentWord == word:
                return True
            ans = False
            for nextRow,nextCol in [(currentRow+1,currentCol),(currentRow-1,currentCol),(currentRow,currentCol+1),(currentRow,currentCol-1)]:
                if not(0<=nextRow<m and 0<=nextCol<n) or board[nextRow][nextCol] == " ":
                    continue
                if not(word.startswith(currentWord+board[nextRow][nextCol])):
                    continue
                ans = ans or dfs(nextRow,nextCol,wordTillHere+charHere)
                if ans:
                    break
            board[currentRow][currentCol] = charHere
            return ans
        s = Counter(word)
        if s[word[0]] > s[word[-1]]:
            word = word[::-1]
        ans = False
        for rowIndex in range(m):
            for colIndex in range(n):
                if not(word[0] == board[rowIndex][colIndex]):
                    continue
                ans = ans or dfs(rowIndex,colIndex,"")
        return ans
