#attempt1:
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for operation in ops:
            if operation.isdigit() or operation[0] == "-":
                stack.append(int(operation))
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(stack[-1]+stack[-2])
            #print(stack)
        return sum(stack)
            
        
