class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans=0
        words1={n:(len(i),set(i)) for n,i in enumerate(words)}
        for i in words1:
            for j in words1:
                if not(words1[i][1]&words1[j][1]):
                    ans=max(ans,words1[i][0]*words1[j][0])
        return ans