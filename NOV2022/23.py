#attempt1:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lenOfBoard = 9
        def checkRow(rowNumber):
            allNumbersInRow = set()
            for column in range(lenOfBoard):
                if board[rowNumber][column] == ".":
                    continue
                if board[rowNumber][column] in allNumbersInRow:
                    return False
                allNumbersInRow.add(board[rowNumber][column])
            return True
        def checkCol(colNumber):
            allNumbersInCol = set()
            for row in range(lenOfBoard):
                if board[row][colNumber] == ".":
                    continue
                if board[row][colNumber] in allNumbersInCol:
                    return False
                allNumbersInCol.add(board[row][colNumber])
            return True
        def checkIn3x3(rowStart,colStart):
            allNumbersInSubgrid = set()
            for row in range(rowStart, rowStart+3):
                for col in range(colStart,colStart+3):
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in allNumbersInSubgrid:
                        return False
                    allNumbersInSubgrid.add(board[row][col])
            return True
        ans = True
        for row in range(lenOfBoard):
            ans = ans and checkRow(row)
        for col in range(lenOfBoard):
            ans = ans and checkCol(col)
        for row in [0,3,6]:
            for col in [0,3,6]:
                ans = ans and checkIn3x3(row,col)
        return ans
