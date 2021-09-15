#attempt1:
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        ans=1
        diffs=[]
        if n==1:
            return 1
        
        #-1 if a[i] > a[i+1], 1 if a[i]<a[i+1] and 0 otherwise
        flag=0
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                diffs.append(-1)
                flag=1
            elif arr[i]<arr[i+1]:
                diffs.append(1)
                flag=1
            else:
                diffs.append(0)
        #print(diffs)
        if flag:
            ans=2
            curlen=0
            prev=2
            for i in diffs:
                if i==0:
                    ans=max(ans,curlen+1)
                    prev=2
                    curlen=0
                elif prev==2 or prev==-i:
                    curlen+=1
                    prev=i
                else:
                    ans=max(ans,curlen+1)
                    prev=i
                    curlen=1
            ans=max(ans,curlen+1)
            return ans
        else:
            return 1