#attempt1:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        prevRow = []
        for number in range(1,numRows+1):
            currow = [0]*number
            for col in range(1,number-1):
                currow[col] = prevRow[col-1]+prevRow[col]
            currow[0] = 1
            currow[-1] = 1
            ans.append(currow)
            prevRow = currow
        return ans
            
