#attempt3:
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        startIndex, endIndex = -1,-1
        joiningStarted = False
        added = False
        if not(intervals):
            return [newInterval]
        for index, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                joiningStarted = False
                ans.append(interval.copy())
            elif interval[1] < newInterval[0]:
                joiningStarted = False
                ans.append(interval.copy())
            elif interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1]:
                if joiningStarted:
                    ans[-1][0] = min(ans[-1][0],newInterval[0],interval[0])
                    ans[-1][1] = max(ans[-1][1],newInterval[1],interval[1])
                else:
                    ans.append([min(newInterval[0],interval[0]), max(newInterval[1],interval[1])])
                    joiningStarted = True
                added = True
        toBeAddedBefore = len(ans)
        #print(ans)
        if not(added):
            for index in range(len(ans)):
                if ans[index][0] > newInterval[1]:
                    toBeAddedBefore = index
                    break
            ans = ans[:toBeAddedBefore] + [newInterval] + ans[toBeAddedBefore:]
        return ans

        

#attempt1&2: Runtime Error : because we need to have [] around  newInterval
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        startIndex, endIndex = -1,-1
        joiningStarted = False
        added = False
        if not(intervals):
            return [newInterval]
        for index, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                joiningStarted = False
                ans.append(interval.copy())
            elif interval[1] < newInterval[0]:
                joiningStarted = False
                ans.append(interval.copy())
            elif interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1]:
                if joiningStarted:
                    ans[-1][0] = min(ans[-1][0],newInterval[0],interval[0])
                    ans[-1][1] = max(ans[-1][1],newInterval[1],interval[1])
                else:
                    ans.append([min(newInterval[0],interval[0]), max(newInterval[1],interval[1])])
                    joiningStarted = True
                added = True
        toBeAddedBefore = -1
        if not(added):
            for index in range(len(ans)):
                if ans[index][0] > newInterval[1]:
                    toBeAddedBefore = index
                    break
            ans = ans[:toBeAddedBefore] + newInterval + ans[toBeAddedBefore:]
        return ans

        
'''
