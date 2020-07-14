#https://leetcode.com/articles/arranging-coins/
#My solution->naive approach
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        norows=0
        nocoins=0
        while(nocoins+i<=n):
            nocoins+=i
            i+=1
            norows+=1
        return norows

#better approach-> as given in the editorial
#k(k+1)<=2*n
#Completing the squares method
#k=floor(root(2n+0.25)-0.5)
import math
class Solution:
    def arrangeCoins(self,n:int)->int:
        return math.floor((2*n+0.25)**0.5-0.5)
        
