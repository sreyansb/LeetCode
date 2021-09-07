#attempt1:
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans=keysPressed[0]
        maxtime=releaseTimes[0]
        for i in range(1,len(keysPressed)):
            if releaseTimes[i]-releaseTimes[i-1]>maxtime:
                ans=keysPressed[i]
                maxtime=releaseTimes[i]-releaseTimes[i-1]
            elif releaseTimes[i]-releaseTimes[i-1]==maxtime:
                ans=max(ans,keysPressed[i])
        return ans