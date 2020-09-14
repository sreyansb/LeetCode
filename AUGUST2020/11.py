#attempt 2: my code
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not(citations):
            return 0
        citations.sort(reverse=True)
        n=len(citations)
        citations.append(-1)
        answer=0 if citations[0]!=0 else -1
        for i in range(n):
            if citations[i+1]>i+1:
                answer+=1
                continue
            else:
                return answer+1
        
            
            

#attempt 1 : had to take help
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


            
            
            
            
