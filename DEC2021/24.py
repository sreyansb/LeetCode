#attempt1:
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0],x[1]))
        finintervals = []
        curs,cure = intervals[0]
        for starti,endi in intervals[1:]:
            if starti>cure:
                finintervals.append([curs,cure])
                curs,cure = starti,endi
            else:
                cure = max(cure,endi)
        finintervals.append([curs,cure])
        return finintervals
            
        
