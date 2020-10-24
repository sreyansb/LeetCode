#attempt1: 75%, greedy approach->took help, unable to think
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        n=len(tokens)
        if not(n):
            return 0
        tokens.sort()
        maxs=0
        curs=0
        i=0
        j=n-1
        while(i<=j):
            flag=1
            if P>=tokens[i]:
                curs+=1
                P-=tokens[i]
                i+=1
                flag=0
            elif curs>0:
                curs-=1
                P+=tokens[j]
                j-=1
                flag=0
            if flag:#because there is no operation-> aage bhi nahi hoga
                break
            maxs=max(curs,maxs)
        return maxs
