#attempt1:
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        net_cost = [gas[i] - cost[i] for i in range(len(cost))]
        net_cost = net_cost + net_cost[:-1]
        index = 0
        ans = 0
        current_cost = 0
        while (index < len(net_cost)):
            if index - ans + 1 == n:
                break
            
            current_cost += net_cost[index]
            #print(current_cost,index)
            if current_cost < 0:
                ans = index + 1
                current_cost = 0
            index += 1
        return ans
            

        


        
