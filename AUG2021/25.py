#attempt2: 70%
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s=set()
        i=0
        while(i*i<=c):
            s.add(i*i)
            i+=1
        for square in s:
            if c-square in s:
                return True
        return False

#attempt1: 7% Very slow: we dont need to find all sqaures till 2^31
#We need only until c^(0.5)
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s=set()
        i=0
        while(i*i<(1<<31)):
            s.add(i*i)
            i+=1
        for square in s:
            if c-square in s:
                return True
        return False
''' 