#attempt1:
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if not(stack) or abs(ord(stack[-1])-ord(char)) != 32:
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)
