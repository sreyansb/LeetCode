#attempt1: TOOK HINT, very easy problem
#it is about proving if k palindromic strings can be made
#So if number of elements with odd number of occurences>k
#implies we cannot build k palindromic strings
#because each palindromic string has atmost 1 character with odd nummber of
#occurences
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n=len(s)
        if k>n:
            return False
        di={}
        for i in s:
            if i not in di:
                di[i]=0
            di[i]+=1
        count1=0
        for i in di:
            if di[i]&1:
                count1+=1
        if count1>k:
            return False
        return True
         