class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index=list(range(len(intervals)))
        endindex=[i[0] for i in intervals]
        zipperend=list(zip(endindex,index))
        zipperend.sort(key=lambda x:x[0])
        ans=[-1 for i in range(len(intervals))]
        for i in range(len(intervals)):
            low=0
            high=len(intervals)-1
            while(low<=high):
                mid=(low+high)//2
                if zipperend[mid][0]>=intervals[i][1]:
                    ans[i]=zipperend[mid][1]
                    high=mid-1
                if zipperend[mid][0]<intervals[i][1]:
                    low=mid+1
        return ans
        
        
        
        
