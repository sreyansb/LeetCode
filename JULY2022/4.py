#attempt1:
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        ansleft = [1]*n
        ansright = [1]*n
        if ratings[0] > ratings[1]:
            ansleft[0] = ansleft[1]+1
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                ansleft[i] = ansleft[i-1]+1
        if ratings[-1] > ratings[-2]:
            ansleft[-1] = max(ansleft[-1],ansleft[-2]+1)
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                ansleft[i] = max(ansleft[i],ansleft[i+1]+1)
        return sum(ansleft)
        
        
