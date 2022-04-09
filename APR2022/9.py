#attempt1: Used Counter. Checked out help section of COunter on Python
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        return [x[0] for x in s.most_common(k)]
        
