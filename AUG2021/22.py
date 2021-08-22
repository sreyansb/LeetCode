#attempt1: TOOK HELP
# A very difficult problem
#The thing is you need to partition based on heights but not from 1 to 1e9
#Only the heights which appear in the points
# Partition based on start and end points and see which are active and calculate
#the area of all rectangles which have that particular height
#SO first sort based on height and push to currently active stack
# and using merging of intervals (to prevent overlaps), calculate for each height

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod=1000000007
        def merge(arr):
            if not(arr):
                return 0
            prevs,preve=arr[0]
            final=[]
            for i in arr[1:]:
                if i[0]>=preve:
                    final.append([prevs,preve])
                    prevs,preve=i
                else:
                    preve=max(preve,i[1])
            final.append([prevs,preve])
            #print(final)
            ans=0
            for xs,xe in final:
                ans+=(xe-xs)
            #print(ans)
            return ans
        
        newo=[]
        for x1,y1,x2,y2 in rectangles:
            newo.append([y1,0,x1,x2]) #0 is for start
            newo.append([y2,1,x1,x2])
        newo.sort()
        
        ans=0
        tomerge=[]
        prev=0#we need prev because area is between 2 Ys i.e. heights
        for i in newo:
            
            ans+=(i[0]-prev)*merge(tomerge)
            if i[1]==0: #start
                
                tomerge.append([i[2],i[3]])
                tomerge.sort()
            else:
                
                tomerge.remove([i[2],i[3]])
            #print(i,tomerge,ans,prev)
            prev=i[0]
            
        return ans%mod