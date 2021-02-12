#attempt1:
class Solution:
    def numberOfSteps (self, num: int) -> int:
        nosteps=0
        while(num):
            if num&1:
                num-=1
            else:
                num=num>>1
            nosteps+=1
        return nosteps
        
