#attempt2:10%
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        vals=list(range(26,0,-1))
        def greedy(n,value):
            #print(n,value)
            if n==1:#when n==0-> 0<=value<26
                return chr(96+value)
            for i in vals:
                if value-i<(n-1):
                    continue
                if value-i==n-1:
                    return "a"*(n-1)+chr(96+i)
                return greedy(n-1,value-i)+chr(96+i)
        return greedy(n,k)
'''

#attempt1: 5%
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        vals=list(range(26,0,-1))
        def greedy(n,value):
            #print(n,value)
            if n==1:#when n==0-> 0<=value<26
                return chr(96+value)
            for i in vals:
                if value-i<(n-1):
                    continue
                return greedy(n-1,value-i)+chr(96+i)
        return greedy(n,k)
'''
