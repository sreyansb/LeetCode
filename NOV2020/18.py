#attempt1: 50%
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        init=intervals[0]
        n=len(intervals)
        ans=[]
        i=1
        while(i<n):
            if intervals[i][0]>init[1]:
                ans.append(init.copy())
                init=intervals[i]
            else:
                init[1]=max(init[1],intervals[i][1])
            i+=1
        if init:
            ans.append(init.copy())
        return ans
            
            
        
