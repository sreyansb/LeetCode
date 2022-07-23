#attempt1:
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        listlesseronRight = SortedList([])
        ans = []
        for num in nums[::-1]:
            pos = listlesseronRight.bisect_left(num)
            ans.append(pos)
            listlesseronRight.add(num)
        return ans[::-1]
            
        
