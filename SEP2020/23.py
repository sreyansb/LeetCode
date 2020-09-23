#attempt3: took help : it seems : at the last the total cost will be <0 for -1
#i dont know the proof
#67.3% and 88%
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        curcost=0
        index=-1
        ans=float('inf')
        for i in range(n):
            curcost+=gas[i]-cost[i]
            if curcost<=ans:
                index=i
                ans=curcost
        if curcost<0:
            return -1
        return ((index+1)%n)
              
#attempt2: 25%
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        gas+=gas
        cost+=cost
        ans=-1
        answers=[gas[i]-cost[i] for i in range(2*n)]
        for i in range(n):
            curcost=gas[i]-cost[i]
            j=i+1
            while(j<i+n+1 and curcost>=0):
                curcost+=answers[j]
                j+=1
            if curcost>=0:
                ans=i
                break
        return ans
"""             
                
#Attempt 1: 21% and 5.30%
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        gas+=gas
        cost+=cost
        ans=-1
        for i in range(n):
            curcost=gas[i]-cost[i]
            j=i+1
            while(j<i+n+1 and curcost>=0):
                curcost+=gas[j]-cost[j]
                j+=1
            if curcost>=0:
                ans=i
                break
        return ans
"""
