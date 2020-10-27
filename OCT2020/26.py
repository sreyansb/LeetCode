#Attempt1: took a clue. We have to fill the first with poured ml of liquid
#and then divide further
#complicated for no reason
#dpt[i][j] represents the volume of liquid in each that has poured since the
#beginning of the process
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==0 or query_glass>query_row:
            return 0
        if poured==1:
            if query_row==0:
                return 1
            else:
                return 0
        dpt=[[0 for i in range(101)] for j in range(101)]
        dpt[0][0]=poured
        for row in range(1,101):
            dpt[row][0]=(max(0,dpt[row-1][0]-1))/2
            dpt[row][row]=(max(0,dpt[row-1][row-1]-1))/2
            for col in range(1,row):
                dpt[row][col]=(max(0,dpt[row-1][col]-1)+max(0,dpt[row-1][col-1]-1))/2
        return min(1,dpt[query_row][query_glass])
            
        
