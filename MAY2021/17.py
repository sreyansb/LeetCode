#attempt2:
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n=len(words)
        words.sort(key=lambda x:len(x))
        dp={}
        def dpmaker(word):
            res=1
            for j in range(len(word)):
                fin=word[:j]+word[j+1:]
                if fin in dp:
                    res=max(res,dp[fin]+1)
            dp[word]=res
        for i in words:
            dpmaker(i)
        return max(dp.values())


#attempt1:TOOK HINT: GO FROM BACK.**Large strings broken to smaller ones**
#very important
'''
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n=len(words)
        dp={}
        words.sort(key=lambda x:len(x))
        minie=len(words[0])
        for i in words:
            if len(i)==minie:
                dp[i]=1
            else:
                res=1
                for j in range(len(i)):
                    fina=i[:j]+i[j+1:]
                    if fina in dp:
                        res=max(res,dp[fina]+1)
                dp[i]=res
        return max(dp.values())
'''
