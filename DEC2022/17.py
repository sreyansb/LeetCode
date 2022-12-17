#attempt1:
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []
        for i in tokens:
            if i.isdigit() or (i[0] == "-" and i[1:].isdigit()):
                numberStack.append(int(i))
            else:
                rightOperand = numberStack.pop()
                leftOperand = numberStack.pop()
                if i == '+':
                    numberStack.append(leftOperand + rightOperand)
                elif i == '-':
                    numberStack.append(leftOperand - rightOperand)
                elif i == '*':
                    numberStack.append(leftOperand * rightOperand)
                else:
                    numberStack.append(int(leftOperand / rightOperand))
            
        return numberStack[0]
