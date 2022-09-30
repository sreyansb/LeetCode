#attempt1:
from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        entry_exit_height = []
        for entry,exit,height in buildings:
            entry_exit_height.append((entry,'en',height))
            entry_exit_height.append((exit,'ex',-height))
        entry_exit_height.sort(key = lambda x:(x[0],x[1],-x[2]))
        ans = []
        currentStack = SortedList()
        for time,entry_or_exit,height in entry_exit_height:
            if entry_or_exit == 'en':
                prevHeight = currentStack[-1] if currentStack else 0
                currentStack.add(height)
                if prevHeight != currentStack[-1]:
                    ans.append([time,currentStack[-1] if currentStack else 0])
            else:
                currentStack.remove(-height)
                if not(currentStack) or currentStack[-1] < -height:
                    ans.append([time,currentStack[-1] if currentStack else 0])
            
        return ans
        
