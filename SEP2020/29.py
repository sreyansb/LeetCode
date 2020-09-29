#Attempt2: had attempted the problem before, couldn't remember
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}
        def helper(stringy):
            if stringy=="":
                return True
            if stringy in memo:
                return memo[stringy]
            for i in range(1,len(stringy)+1):
                if stringy[:i] in wordDict:
                    memo[stringy[:i]] = True
                    k = helper(stringy[i:])
                    if k:
                        memo[stringy[i:]]=True
                        return True
                    else:
                        memo[stringy[i:]]=False
            return False
        return(helper(s))
        #print(k,memo)

#attempt1: already  had solved the problem before
"""
def wordie(s,worddict,memo):
    if s=="":
        return True
    if (s,True) in memo:
        return True
    if (s,False) in memo:
        return False
    for i in range(1,len(s)+1):
        if s[:i] in worddict:
            memo.add((s[:i],True))
            k=wordie(s[i:],worddict,memo)
            if k:
                memo.add((s[i:],True))
                return True
            else:
                memo.add((s[i:],False))
    return False
            
            
    
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict=set(wordDict)
        return wordie(s,wordDict,set())
"""
obj=Solution()
print(obj.wordBreak("aaaaaaa",["aaaa","aaa"]))
