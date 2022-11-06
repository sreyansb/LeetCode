#attempt2: anything with k>1 can be sorted
from heapq import heappush,heappop
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        heap = []
        n = len(s)
        if k > 1:
            return "".join(sorted(s))
        for index in range(k):
            heappush(heap,(-ord(s[index]),index))
        seenWords = set()
        ans = s
        while(s not in seenWords):
            seenWords.add(s)
            largeCharAscii,index = heappop(heap)
            nextString = s[:index]+s[index+1:]+chr(-largeCharAscii)
            s = nextString
            ans = min(ans,s)
            heap = []
            for index in range(k):
                heappush(heap,(-ord(s[index]),index))
        return ans



#attempt1: WA because I thought largest element will be appended at the back
'''
from heapq import heappush,heappop
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        heap = []
        n = len(s)
        for index in range(k):
            heappush(heap,(-ord(s[index]),index))
        seenWords = set()
        ans = s
        while(s not in seenWords):
            seenWords.add(s)
            largeCharAscii,index = heappop(heap)
            nextString = s[:index]+s[index+1:]+chr(-largeCharAscii)
            s = nextString
            ans = min(ans,s)
            heap = []
            for index in range(k):
                heappush(heap,(-ord(s[index]),index))
        return ans


'''
