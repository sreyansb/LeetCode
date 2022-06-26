#attempt1:
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        frontscore = [cardPoints[0]]*n
        for i in range(1,n):
            frontscore[i] = cardPoints[i]+frontscore[i-1]
        backscore = [cardPoints[-1]]*n
        for i in range(n-2,-1,-1):
            backscore[i] = cardPoints[i]+backscore[i+1]
        maxscore = -float('inf')
        
        for elements_from_front in range(1,(k//2)+1):
            elements_from_back = k - elements_from_front
            maxscore = max(maxscore,frontscore[elements_from_front-1]+backscore[n-elements_from_back],frontscore[elements_from_back-1]+backscore[n-elements_from_front])
        maxscore = max(maxscore,frontscore[k-1],backscore[n-k])
        return maxscore
            
            
        
