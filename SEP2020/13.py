#attempt1 : 96% and 88% Just insert and sort and and then check
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        ans=[]
        intervals.sort(key=lambda x:x[0])
        newInterval=intervals[0]
        for i in intervals[1:]:
            if i[0]>newInterval[1]:
                ans.append(newInterval)
                newInterval=i
            else:
                newInterval=[min(i[0],newInterval[0]),max(i[1],newInterval[1])]
        ans.append(newInterval)
        return ans
            
            
                
                
