#attempt4:TOOK HELP DP
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp={}
        strs=[(x.count('0'),x.count('1')) for x in strs]
        n1=len(strs)
        def dpc(mleft,nleft,pairs):
            if mleft<0 or nleft<0:
                return -1
            if pairs==n1:
                return 0
            if (mleft,nleft,pairs) in dp:
                return dp[mleft,nleft,pairs]
            dp[(mleft,nleft,pairs)]=max(1+dpc(mleft-strs[pairs][0],nleft-strs[pairs][1],pairs+1),dpc(mleft,nleft,pairs+1))
            return dp[(mleft,nleft,pairs)]
        return dpc(m,n,0)

#attempt3: Very important to sort using both based on 0 and 1
from heapq import heappush,heappop
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zo=[(x.count("0"),x.count("1")) for x in strs]
        zo.sort(key=lambda x:(x[0],x[1]))
        n1=len(zo)
        def check(zo):
            ans1=0
            for i in range(n1):
                ans=[]
                totalz,totalo=0,0
                if totalz+zo[i][0]>m or totalo+zo[i][1]>n:
                    continue
                totalz+=zo[i][0]
                totalo+=zo[i][1]
                heappush(ans,(-totalz,-totalo))
                for j in range(i+1,n1):
                    if totalo+zo[j][1]<=n and totalz+zo[j][0]<=m:
                        totalo+=zo[j][1]
                        totalz+=zo[j][0]
                        heappush(ans,(-zo[j][0],-zo[j][1]))
                    else:
                        if zo[j][0]<=-ans[0][0] and zo[j][1]<=-ans[0][1]:
                            k=heappop(ans)
                            heappush(ans,(-zo[j][0],-zo[j][1]))
                            totalz=totalz+k[0]+zo[j][0]
                            totalo=totalo+k[1]+zo[j][1]
                    #print(i,ans,zo[j],totalz,totalo)
                ans1=max(len(ans),ans1)
                #print(ans1,len(ans),i,ans,totalz,totalo)
            return ans1
        ans1=check(zo)
        ans2=check(sorted(zo,key=lambda x:(x[1],x[0])))
        return max(ans1,ans2)

#attempt1&2: WA
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zo=[(x.count("0"),x.count("1")) for x in strs]
        zo.sort(key=lambda x:(x[0],x[1]))
        #print(zo)
        ans=[]
        count=0
        totalz=0
        totalo=0
        for i in zo:
            if totalz+i[0]<=m and totalo+i[1]<=n:
                totalz+=i[0]
                totalo+=i[1]
                count+=1
        count1=0
        totalz,totalo=0,0
        zo.sort(key=lambda x:(x[1],x[0]))
        for i in zo:
            if totalz+i[0]<=m and totalo+i[1]<=n:
                totalz+=i[0]
                totalo+=i[1]
                count1+=1
        return max(count,count1)
        
'''
