#attempt1:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        current = 0
        n = len(s)
        stack = []
        arr = [0]*n
        for index in range(n):
            i = s[index]
            if i == "(":
                stack.append(index)
                arr[index] = -1
            else:
                if stack:
                    indi = stack.pop()
                    arr[indi] = 1
                else:
                    current = 0
                    arr[index] = -1
        for index in range(n):
            if arr[index]:
                if arr[index] == -1:
                    current = 0
                else:
                    current += 2
                ans = max(ans,current)
        return ans
            
