#attempt1:
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0]*n
        for index in range(n-1,-1,-1):
            while(stack and stack[-1][0] <= temperatures[index]):
                stack.pop()
            if stack:
                ans[index] = stack[-1][1]-index
            stack.append((temperatures[index],index))
        return ans
        
