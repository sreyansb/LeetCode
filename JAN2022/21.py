#attempt3: O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        n = len(gas)
        start = 0
        cur = 0
        for i in range(n):
            cur += gas[i] - cost[i]
            if cur<0:
                cur = 0
                start = i+1
        return start%n

#attempt2: O(n^2)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        n = len(gas)
        for i in range(n):
            curcost = gas[i]-cost[i]
            j = (i+1)%n
            while(curcost>0 and j!=i):
                curcost += gas[j]-cost[j]
                j = (j+1)%n
            if j==i:
                return i
        return -1

#attempt1:WA : curindex should become i+1 because 0...i is not good enough
#Since sum of gas>sum of cost => the journey is 100% possible
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        n = len(gas)
        curindex = 0
        cursum = 0
        for i in range(n):
            cursum += gas[i] - cost[i]
            if cursum<0:
                curindex += 1
        return curindex-1 if curindex<=n else -1
            
            
'''
