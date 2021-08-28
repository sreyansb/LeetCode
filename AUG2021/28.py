#attempt2: Based my recursion on index i.e. the amount of value that can be taken
#starting from current index(could include this index's profit
#(then it should start from the index which has start time>=endTime of current index))
# if doesn't include this index=> take next index
from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(startTime)
        tep=[[startTime[i],endTime[i],profit[i]] for i in range(n)]
        tep.sort(key=lambda x:x[0])
        startTime.sort()
        @lru_cache(None)
        def recurse(index):
            if index>=n:
                return 0
            newindex=bisect_left(startTime,tep[index][1])
            ans=-float('inf')
            ans=max(tep[index][-1]+recurse(newindex),recurse(index+1))
            return ans
        return recurse(0)

#attempt1:TLE I was doing using endtime, should be based on index
'''
from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(startTime)
        tep=[[startTime[i],endTime[i],profit[i]] for i in range(n)]
        tep.sort(key=lambda x:x[0])
        startTime.sort()
        @lru_cache(None)
        def recurse(endtime):
            index=bisect_left(startTime,endtime)
            if index>=n:
                return 0
            ans=-float('inf')
            for i in range(index,n):
                ans=max(ans,tep[i][-1]+recurse(tep[i][1]))
            return ans
        return recurse(0)
'''