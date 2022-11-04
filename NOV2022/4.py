#attempt2: AC
class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = [index for index in range(len(s)) if s[index] in "aeiouAEIOU"]
        newString = list(s)
        start = 0
        end = len(stack)-1
        while(start < end):
            newString[stack[start]],newString[stack[end]] = newString[stack[end]],newString[stack[start]]
            start += 1
            end -= 1
        return "".join(newString)

#attempt1: WA because didn't take care of capital letters
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = [index for index in range(len(s)) if s[index] in "aeiou"]
        newString = list(s)
        start = 0
        end = len(stack)-1
        while(start < end):
            newString[stack[start]],newString[stack[end]] = newString[stack[end]],newString[stack[start]]
            start += 1
            end -= 1
        return "".join(newString)
'''
