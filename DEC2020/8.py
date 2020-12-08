#attempt1:
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        times=[0 for i in range(60)]
        for i in time:
            times[i%60]+=1
        ans=max(0,times[0]*(times[0]-1)/2)+max(0,times[30]*(times[30]-1)/2)
        for i in range(1,30):
            ans+=(times[i]*times[60-i])
        return int(ans)
            
            
