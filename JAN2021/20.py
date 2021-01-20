#attempt1: remember for length=1
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            elif i=="]":
                if stack and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
            elif i=="}":
                if stack and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not(stack) else False
                                           
            
        
