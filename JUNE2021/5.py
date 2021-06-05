#attempt2: IT is atmost k engineers so maintain a heap and do it . It is not always
#maxheap, maintain a min heap and remove smallest element everytime
#REMEMBER MOD
from heapq import heappush,heappop
class Solution:
    def maxPerformance(self, number: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engefi=[(speed[i],n) for i,n in enumerate(efficiency)]
        engefi.sort(key=lambda x:(x[1],x[0]))
        curs=[]
        summy=0
        maxie=0
        for i in range(number-1,-1,-1):
            maxie=max(maxie,(engefi[i][0]+summy)*engefi[i][1])
            summy+=engefi[i][0]
            heappush(curs,engefi[i][0])
            if len(curs)==k:
                summy-=heappop(curs)
            #print(curs)
        return maxie%(10**9+7)        

#attempt1: Thought that it is =k the number of engineers. SOmehow it would give TLE
    
'''
from sortedcontainers import SortedList
class Solution:
    def maxPerformance(self, number: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engefi=[(speed[i],n) for i,n in enumerate(efficiency)]
        engefi.sort(key=lambda x:(x[1],x[0]))
        speeds=SortedList([engefi[x][0] for x in range(number-k+1,number)])
        maxie=0
        for i in range(number-k,-1,-1):
            summy=sum(speeds[-k+1:])
            maxie=max(maxie,(summy+engefi[i][0])*engefi[i][1])
            speeds.add(engefi[i][0])
        return maxie

'''
