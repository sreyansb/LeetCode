#attempt2: TOOK HELP very important problem
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        lens=[0]
        n=len(S)
        for i in S:
            if i.isalpha():
                lens.append(lens[-1]+1)
            else:
                lens.append(lens[-1]*int(i))
        for i in range(n,0,-1):
            K%=lens[i]
            if K==0 and S[i-1].isalpha():
                return S[i-1]
        


#attempt1: TLE and Memory Error 33/45
'''
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        stack=[]
        for i in S:
            if i.isalpha():
                stack.append(i)
            else:
                stack=stack*int(i)
            if len(stack)>=K:
                return stack[K-1]
        #print(stack)
        return stack[K-1]
        
'''
