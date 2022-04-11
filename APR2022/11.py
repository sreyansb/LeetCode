#aattempt1:
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rowl = len(grid)
        coll = len(grid[0])
        k %= (rowl*coll)
        newarr = [[-1 for i in range(coll)] for j in range(rowl)]
        row_addition = k//coll
        col_addition = k%coll
        for row in range(rowl):
            for col in range(coll):
                fincol = (col+col_addition)
                carry = 0
                if fincol >= coll:
                    carry = 1
                    fincol %= coll
                finrow = (row+row_addition+carry)%rowl
                newarr[finrow][fincol] =grid[row][col]
        return newarr
                
        
