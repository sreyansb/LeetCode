#ATTEMPT2: It is a scheduling problem - 70% and 75%
#It is all based on reverse sorting of intervals based on x[0]
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x:x[0],reverse=True)
        #intervals[i][0]>=intervals[j][0] and intervals[j][1]>=intervals[i][1]
        #above condition should hold true for overlap of intervals[i]
        for i in range(n-1):
            flag=0
            for j in range(i+1,n):
                if intervals[j][1]>=intervals[i][1]:
                    flag=1
                    break
            if flag:
                intervals[i]=""
        return len([i for i in intervals if i])

#ATTEMPT1: Accepted 5% and 32%
"""
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        for i in range(n):
            if not(intervals[i]):
                continue
            flag=0
            for j in range(n):
                if i==j or not(intervals[j]):
                    continue
                if intervals[j][0]<=intervals[i][0] and intervals[i][1]<=intervals[j][1]:
                    flag=1
                    break
            if flag:
                intervals[i]=""
        return len([i for i in intervals if i])
"""
