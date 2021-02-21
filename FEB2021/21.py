#attempt1: Took Help always to convert source number to target number
#try converting target number to source number by doing opposite operations
#For example, here if target is odd, there is no way but to add a number to it
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        steps=0
        while(Y>X):
            if Y&1:
                Y+=1
            else:
                Y//=2
            steps+=1
        return steps+X-Y
                
        
