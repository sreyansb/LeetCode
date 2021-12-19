#attempt2: AC
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isdigit():
                if stack and str(stack[-1]).isdigit():
                    stack[-1] = stack[-1]*10+int(i)
                else:
                    stack.append(int(i))
            elif i == ']':
                curstr = ""
                while(stack[-1]!="["):
                    curstr += stack.pop()[::-1]
                stack.pop()
                curstr = curstr*stack.pop()
                stack.append(curstr[::-1])
            else:
                stack.append(i)
        return "".join(stack)
                    
#attempt1: Runtime Error 100[leetcode] : 1 is int in the stack and isdigit() can't be done
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isdigit():
                if stack and stack[-1].isdigit():
                    stack[-1] = stack[-1]*10+int(i)
                else:
                    stack.append(int(i))
            elif i == ']':
                curstr = ""
                while(stack[-1]!="["):
                    curstr += stack.pop()[::-1]
                stack.pop()
                curstr = curstr*stack.pop()
                stack.append(curstr[::-1])
            else:
                stack.append(i)
        return "".join(stack)
'''
