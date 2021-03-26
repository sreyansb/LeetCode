#attempt1: TOOK HELP: It depends on the differences only.
#see you would always need to have to be dependent on differences.
#So if a difference has already been seen, you would have to multiply
#the number of occurences by 26 and add the difference
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t):
            return False
        n=len(s)
        if not(n):
            return True
        ans=[0 for i in range(26)]
        for _ in range(n):
            i=(-ord(s[_])+ord(t[_]))%26
            if i and 26*ans[i]+i>k:
                return False
            ans[i]+=1
        return True
