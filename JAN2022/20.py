#attempt1:
from bisect import bisect_right
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = 10**9
        piles.sort()
        ans = -1
        n = len(piles)
        while(start<=end):
            mid = (start+end)>>1
            pos = bisect_right(piles,mid)
            elems_needed = pos
            while(pos<n and elems_needed<=h):
                elems_needed += ceil(piles[pos]/mid)
                pos += 1
            if elems_needed<=h:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
