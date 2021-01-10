#attempt3:
from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        finans=SortedList()
        totcost=0
        n=0
        mod=1000000007
        di={}
        for i in instructions:
            if i not in di:
                di[i]=0
            di[i]+=1
            finans.add(i)
            n+=1
            j=finans.bisect_left(i)
            totcost+=min(max(0,j),max(0,n-j-di[i]))
            totcost%=mod
            #print(i,totcost)
        return totcost%mod

#attempt2: TLE 56/65
'''
from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        finans=SortedList()
        totcost=0
        n=0
        for i in instructions:
            totcost+=min(bisect_left(finans,i),n-bisect_right(finans,i))
            n+=1
            finans.add(i)            
            #print(i,totcost)
        return totcost%(1000000007)
        
'''

#attempt1: O(n^2 lg(n)) algo - TLE 46/65
'''
from heapq import heappush,heappop
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        smaller=[]
        larger=[]
        totcost=0
        for i in instructions:
            ns,nl,nos,nol=[],[],0,0
            while(smaller):
                k=heappop(smaller)
                heappush(ns,k)
                if k>=i:
                    break
                nos+=1
            while(larger):
                k=heappop(larger)
                heappush(nl,k)
                if -k<=i:
                    break
                nol+=1
            totcost+=min(nos,nol)
            while(ns):
                heappush(smaller,heappop(ns))
            while(nl):
                heappush(larger,heappop(nl))
            heappush(smaller,i)
            heappush(larger,-i)
        return totcost%(1000000007) 
'''
