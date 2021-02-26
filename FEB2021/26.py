#attempt1:
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed==popped:
            return True
        stack=[]
        poj=0
        puj=0
        while(puj<len(pushed)):
            stack.append(pushed[puj])
            while (stack and stack[-1]==popped[poj]):
                stack.pop()
                poj+=1
            puj+=1
        if stack:
            return False
        return True
