#attempt1:
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        moreRocks = [capacity[i]-rocks[i] for i in range(n)]
        moreRocks.sort()
        index = 0
        while(index<n and additionalRocks):
            if additionalRocks < moreRocks[index]:
                break
            additionalRocks -= moreRocks[index]
            index += 1
        return index
