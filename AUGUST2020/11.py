class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not(citations):
            return 0
        citations.sort()
        n=len(citations)
        h=0
        for i in range(n-1,-1,-1):
            count=n-i
            if count<=citations[i]:
                h=count
            else:
                break
        return h
            
            
            
            
