#attempt2: For each index of word: try having it/not having it.
#remove if not using it makes sense
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        j=1
        strleng=len(strs[0])
        n=len(strs)
        ans=0
        while(j<=strleng):
            newlist=[strs[i][:j] for i in range(n)]
            if newlist==sorted(newlist):
                j+=1
                continue
            ans+=1
            strs=[strs[i][:j-1]+strs[i][j:] for i in range(n)]
            strleng-=1
        return ans

#attempt1: Wrong attempt because not deleting efficiently
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        strleng=len(strs[0])
        notallowedindices=0
        for j in range(strleng):
            curmin=strs[0][j]
            notallow=0
            equal=0
            for i in range(1,n):
                if strs[i][j]>curmin:
                    continue
                elif strs[i][j]==curmin:
                    equal=1
                else:
                    notallow=1
                    break
            if notallow:
                notallowedindices+=1
                continue
            if not equal:
                break
        return notallowedindices
'''