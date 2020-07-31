#ACCEPTED:
def wordie(s,worddict,memo,answer):
    #print(s,memo)
    #print(s,memo)
    if s=="":
        return ['']  
    if s in memo:
        return memo[s]
    res=[]
    for i in range(1,len(s)+1):
        if s[:i] in worddict:
            k=wordie(s[i:],worddict,memo,answer)
            print(k)
            res.append((s[:i] + " " + k[0]).strip())       
    memo[s]=res
    #print(s,memo[s])
    return memo[s]
        
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict=set(wordDict)
        answer=[]
        sentence=[]
        return wordie(s,wordDict,{},answer)
#Not Accepted
"""
def wordie(s,worddict,memo,answers,sentence):
    #print(s,sentence)
    if s=="":
        return True  
    if s in worddict:
        sentence.append(s)
    for i in range(1,len(s)+1):
        if s[:i] in worddict:
            sentence.append(s[:i])
            if i==len(s):
                answers.add(" ".join(sentence))
                sentence.pop()
            k=wordie(s[i:],worddict,memo,answers,sentence)
            sentence.pop()           
    return False
        
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict=set(wordDict)
        answers=set()
        sentence=[]
        wordie(s,wordDict,{},answers,sentence)
        if sentence:
            answers.add(" ".join(sentence))
        return list(answers)
"""
obj=Solution()
#print(obj.wordBreak("aaaaaaa",["aaaa","aa","a"]))
print(obj.wordBreak("pineapplepenapple",\
                    ["apple", "pen", "applepen", "pine", "pineapple"]))
#print(obj.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
#print(obj.wordBreak("catsandog",["cat", "cats", "and", "sand", "dog"]))
