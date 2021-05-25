#attempt1: Evaluate postfix operation
from math import floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in "+-/*":
                param2=stack.pop()
                param1=stack.pop()
                if i=='+':
                    stack.append(param1+param2)
                if i=='-':
                    stack.append(param1-param2)
                if i=='/':
                    stack.append(int(param1/param2))
                if i=='*':
                    stack.append(param1*param2)
            else:
                stack.append(int(i))
            #print(stack)
        return stack[0]