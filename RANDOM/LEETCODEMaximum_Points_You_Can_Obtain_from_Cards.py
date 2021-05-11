#attempt1: TOOK HINT - So we need to make the stuff from intial and end points
#so we need to choose a contiguous subarray of least sum from the remaining n-k
#elements
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        tot=sum(cardPoints)
        n=len(cardPoints)
        ksum=sum(cardPoints[:k])
        kcopy=k
        ans=float('inf')
        while(k+1):
            cursum=tot-ksum
            ans=min(ans,cursum)
            ksum=ksum+cardPoints[n-1-(kcopy-k)]-cardPoints[k-1]
            k-=1
        return tot-ans
        
        
