#attempt2: TOOK HELP
#We dont bother about who is playing the chance as we subtract the next person's best choice from the current player.
#We can optimize by keeping DP table because that is all we need.
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        mini=[float('inf')]
        n=len(stones)
        dp=[[-1 for i in range(n)]for j in range(n)]
        def check(start,end,summy):
            if start<0 or end>=n:
                return -float('inf')
            if start>end:
                return 0
            if dp[start][end]==-1:
                dp[start][end]=max(summy-stones[start]-check(start+1,end,summy-stones[start]),summy-stones[end]-check(start,end-1,summy-stones[end]))
            return dp[start][end]
        return check(0,n-1,sum(stones))


#attempt1: WA because I didnt consider that both play optimally
'''
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        mini=[float('inf')]
        n=len(stones)
        def check(start,end,alicesum,bobsum,cursum,turn):
            print(turn,alicesum,bobsum)
            if start<0 or end>=n:
                return
            if start>end:
                if alicesum>bobsum:
                        #print(alicesum,bobsum)
                        mini[0]=min(mini[0],alicesum-bobsum)
                return
            if turn:
                check(start+1,end,alicesum+cursum-stones[start],bobsum,cursum-stones[start],0)
                check(start,end-1,alicesum+cursum-stones[end],bobsum,cursum-stones[end],0)
            else:
                check(start+1,end,alicesum,bobsum+cursum-stones[start],cursum-stones[start],1)
                check(start,end-1,alicesum,bobsum+cursum-stones[end],cursum-stones[end],1)
            return
        check(0,n-1,0,0,sum(stones),1)
        return mini[0]
'''