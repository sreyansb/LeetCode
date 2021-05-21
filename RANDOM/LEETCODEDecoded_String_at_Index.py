class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        n=len(S)
        stack=[0]
        for i in S:
            if i.isalpha():
                stack.append(stack[-1]+1)
            else:
                stack.append(stack[-1]*int(i))
        for i in range(n,0,-1):
            K%=stack[i]
            if K==0 and S[i-1].isalpha():
                return S[i-1]
        
        