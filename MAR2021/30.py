#attempt3: TOOK HELP, it is a Longest Increasing Subsequence(LIS) problem
#First we sort based on width(envelope[index][0] and if widths are same then
#based on descending order of heights.
#Now the width part is removed as every cone higher up in the indices can fit
#a lower cone.
#Now it is a problem of LIS based on heights
#for every index i(0<i<n) find LIS[i] such that LIS[i]=max(LIS[i],LIS[j]+1)
#for all 0<=j<i
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        n=len(envelopes)
        lis=[1]*n
        for i in range(1,n):
            for j in range(i):
                if envelopes[j][1]<envelopes[i][1]:
                    lis[i]=max(lis[i],lis[j]+1)
        return max(lis)

#attempt2:TLE 
'''
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],x[1]),reverse=True)
        #print(envelopes)
        maxie=1
        n=len(envelopes)
        dp=[[-1 for i in range(2)] for j in range(n+10)]#0 when that is the parent and 1 if parent is parent
        k=float('inf')
        def maxiechecker(index,parent=[k,k]):
            if index>=n:
                return 0
            if envelopes[index][0]<parent[0] and envelopes[index][1]<parent[1]:
                if dp[index][0]==-1:
                    dp[index][0]=1+maxiechecker(index+1,envelopes[index])
                dp[index][1]=max(dp[index][1],maxiechecker(index+1,parent))
                return max(dp[index])
            else:
                return maxiechecker(index+1,parent)
                
        k=maxiechecker(0)
        return k
'''

#attempt1:WA - didnt take into consideration the width
'''
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],x[1]),reverse=True)
        maxie=1
        n=len(envelopes)
        print(envelopes)
        if not(n):
            return 0
        index=1
        prev=envelopes[0]
        while(index<n):
            if envelopes[index][0]<prev[0] and envelopes[index][1]<prev[1]:
                maxie+=1
                prev=envelopes[index]
            index+=1
        return maxie
'''
