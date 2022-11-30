#attempt1:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countSeq = Counter(arr)
        return len(countSeq.values()) == len(set(countSeq.values()))
