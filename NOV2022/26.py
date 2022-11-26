#attempt2: TOOK HELP thought of it after submitting
from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        zippedDuration = [(startTime[index],endTime[index],profit[index]) for index in range(n)]
        zippedDuration.sort(key = lambda x:x[0])
        startTime.sort()
        @lru_cache(None)
        def findAns(index = 0):
            if index >= n:
                return 0
            positionInStart = bisect_left(startTime, zippedDuration[index][1])
            return max(findAns(index+1),zippedDuration[index][-1] + findAns(positionInStart))
        return findAns(0)
