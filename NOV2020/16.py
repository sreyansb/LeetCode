#attempt2: 40% and 40%
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        maxl=0
        n=len(A)
        diff=[]
        for i in range(1,n):
            k=A[i]-A[i-1]
            if k>0:
                diff.append(1)
            else:
                diff.append(0)
        curl=0
        decreasestart=0
        #print(diff)
        for i in range(n-1):
            if diff[i]==0 and curl<1:
                curl=0
                continue
            elif diff[i]==0 and curl>=1 and A[i+1]!=A[i]:
                decreasestart=1
                curl+=1
                maxl=max(maxl,curl+1)
            elif diff[i]==0 and curl>=1 and A[i+1]==A[i]:
                curl=0
                decreasestart=0
            elif diff[i]==1:
                if decreasestart:
                    curl=1
                    decreasestart=0
                else:
                    curl+=1
            #print(i,curl)
        return maxl
#attempt1: TLE 9/72 len(A)==10000
"""
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        maxl=0
        n=len(A)
        #print(n)
        for i in range(n-2):
            curl,flag=1,2
            for j in range(i+1,n):
                if A[j]>A[j-1] and flag:
                    curl+=1
                    flag=1
                elif A[j]<A[j-1] and flag==1:
                    curl+=1
                    flag=0
                elif not(flag) and A[j]<A[j-1]:
                    curl+=1
                    maxl=max(maxl,curl)
                else:
                    curl=0
                    break
        return maxl
"""
