#attempt1:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        di = {"}":"{",")":"(","]":"["}
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if not(stack) or stack[-1] != di[i]:
                    return False
                stack.pop()
        if not(stack):
            return True
        return False
                
        
