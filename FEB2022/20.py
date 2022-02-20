#attempt1:
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        numberofintervals = 1
        curs,cure = intervals[0]
        for prec,pree in intervals[1:]:
            if not(curs<=prec and cure>=pree):
                numberofintervals += 1
                curs,cure = prec,pree
        return numberofintervals
                
