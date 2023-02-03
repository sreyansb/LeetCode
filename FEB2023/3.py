#attempt3: AC
from math import ceil
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s
        ans = [""]*numRows
        curRow = 0
        direction = 1
        for char in s:
            if curRow == 0 and direction == -1:
                direction = 1
            if curRow == numRows-1 and direction == -1:
                direction = 1
            ans[curRow] += char
            if curRow == 1 and direction == -1:
                curRow = 0
                direction = 1
            elif curRow == numRows-1 and direction == 1:
                curRow -= 1
                direction = -1
            else:
                curRow += direction
        return "".join(ans)



#attempt2: RunTime Error : need to setup guardrails to ensure everything is right
#for example, at 0th index direction always has to be +1
'''
from math import ceil
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s
        ans = [""]*numRows
        curRow = 0
        direction = 1
        for char in s:
            ans[curRow] += char
            if curRow == 1 and direction == -1:
                curRow = 0
                direction = 1
            elif curRow == numRows-1 and direction == 1:
                curRow -= 1
                direction = -1
            else:
                curRow += direction
        return "".join(ans)


        
'''

