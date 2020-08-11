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

obj=Solution()
print(obj.wordBreak("aaaaaaa",["aaaa","aaa"]))
