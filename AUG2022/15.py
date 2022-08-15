#attempt1:
class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []
        di = {"V":5,"L":50,"D":500}
        for char in s[::-1]:
            if char == 'I':
                if stack:
                    if stack[-1] < 3:
                        stack[-1] += 1
                    else:
                        stack[-1] -= 1
                else:
                    stack.append(1)
            if char in ('V', 'L', 'D'):
                stack.append(di[char])
            if char == 'X':
                if stack and (stack[-1] == 100 or stack[-1] == 50):
                    stack[-1] -= 10
                elif stack and stack[-1]%10 == 0:
                    stack[-1] += 10
                else:
                    stack.append(10)
            if char == "C":
                if stack and (stack[-1] == 1000 or stack[-1] == 500):
                    stack[-1] -= 100
                elif stack and stack[-1]%100 == 0:
                    stack[-1] += 100
                else:
                    stack.append(100)
            if char == "M":
                stack.append(1000)
        return sum(stack)
            
