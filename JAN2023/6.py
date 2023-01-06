#attempt1:
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        index = 0
        while(index < len(costs) and coins):
            if coins < costs[index]:
                break
            coins -= costs[index]
            index += 1
        return index
