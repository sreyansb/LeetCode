#attempt1:
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : -x[1])
        index = 0
        n = len(boxTypes)
        ans = 0
        while(index<n and truckSize>0):
            tsize = min(truckSize,boxTypes[index][0])
            ans += boxTypes[index][1]*tsize
            truckSize -= tsize
            index += 1
        return ans
            
