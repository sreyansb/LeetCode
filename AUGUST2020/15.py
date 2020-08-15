class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #i think this is an approach of scheduling and tasks=> based on the fact that end time ka sorted order.
        #schedule max number of tasks
        if not(intervals):
            return 0
        intervals.sort(key=lambda x:x[1])
        init=intervals[0]
        maxi=1
        for i in intervals[1:]:
            if i[0]>=init[1]:
                maxi+=1
                init=i
        return len(intervals)-maxi
            
        
