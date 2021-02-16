#attempt1:
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n=len(S)
        ans=set()
        for i in S:
            newans=set()
            for words in ans:
                    newans.add(words+i.upper())
                    newans.add(words+i.lower())
            if not(ans):
                newans.add(i.upper())
                newans.add(i.lower())
            ans=newans.copy()
            del newans
            #print(ans)
        return list(ans)
        
        
