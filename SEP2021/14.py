#attempt1:
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack=[]
        for i in s:
            if i.lower() in "qwertyuiopasdfghjklzxcvbnm":
                stack.append(i)
        final=""
        for i in s:
            if i.lower() in "qwertyuiopasdfghjklzxcvbnm":
                final+=stack.pop()
            else:
                final+=i
        return final