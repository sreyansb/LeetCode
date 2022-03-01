#attempt1:
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        currentones = 0
        for i in range(1,n+1):
            #print(i,currentones)
            if i%2==0:
                sub = -1
                while(i%2==0):
                    sub += 1
                    i //= 2
                currentones -= sub
            else:
                currentones += 1
            ans.append(currentones)
        return ans
            
            
            
        
