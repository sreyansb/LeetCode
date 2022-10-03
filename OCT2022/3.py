#attempt1:
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        index = 0
        n = len(colors)
        ans = 0
        while(index < n):
            current = colors[index]
            maxTime = -float('inf')
            sumTime = 0
            while(index < n and colors[index] == current):
                maxTime = max(maxTime,neededTime[index])
                sumTime += neededTime[index]
                index += 1
            ans += sumTime-maxTime
        return ans
                
                
            
            
            
