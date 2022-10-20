#attempt1:
from heapq import heappush,heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        allSeenWords = {}
        for word in words:
            if word not in allSeenWords:
                allSeenWords[word] = 0
            allSeenWords[word] += 1
            heappush(heap,(-allSeenWords[word],word))
        ans = []
        while(k):
            count, word = heappop(heap)
            if word not in allSeenWords:
                continue
            del allSeenWords[word]
            ans.append(word)
            k -= 1
        return ans
