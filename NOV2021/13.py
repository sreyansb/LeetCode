#attempt3: TOOK HELP: Stack based problem, we are concerned with closest greater
#element, typical stack based problem
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #binary search doesn't work because next one could be anywhere
        #similarly heap wouldn't work
        n = len(temperatures)
        ans  = [0 for i in range(n)]
        stack = [(temperatures[-1],n-1)]
        for i in range(n-2,-1,-1):
            temp = temperatures[i]
            while(stack and stack[-1][0]<=temp):
                stack.pop()
            if stack:
                ans[i] = stack[-1][-1] - i
            stack.append((temp,i))
        return ans

#attempt2: TLE TOOK HINT and used sorted list for keys and found it
'''
from sortedcontainers import SortedList
from bisect import bisect_right
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #binary search doesn't work because next one could be anywhere
        #similarly heap wouldn't work
        n = len(temperatures)
        keys = SortedList([])
        ans  = [0 for i in range(n)]
        di = dict()
        di[temperatures[-1]] = n-1
        keys.add(temperatures[-1])
        for i in range(n-2,-1,-1):
            temp = temperatures[i]
            min_pos = n
            for t in keys[keys.bisect_right(temp):]:
                min_pos = min(min_pos,di[t])
            if min_pos != n:
                ans[i] = min_pos - i
            if temp not in di:
                di[temp] = 0
                keys.add(temp)
            di[temp] = i
        return ans
'''

#attempt1: TLE TOOK HINT and used idea of dictionary
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #binary search doesn't work because next one could be anywhere
        #similarly heap wouldn't work
        n = len(temperatures)
        ans  = [0 for i in range(n)]
        di = dict()
        di[temperatures[-1]] = n-1
        for i in range(n-2,-1,-1):
            temp = temperatures[i]
            min_pos = n
            for t in di:
                if t>temp:
                    min_pos = min(min_pos,di[t])
            if min_pos != n:
                ans[i] = min_pos - i
            if temp not in di:
                di[temp] = 0
            di[temp] = i
        return ans
'''