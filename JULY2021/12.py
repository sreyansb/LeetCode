#attempt1:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        di={}
        dit={}
        for i in range(n):
            if s[i] in di:
                if di[s[i]]==t[i] and dit[t[i]]==s[i]:
                    di[s[i]]=t[i]
                else:
                    return False
            else:
                if t[i] in dit:
                    return False
                else:
                    di[s[i]]=t[i]
                    dit[t[i]]=s[i]
        return True
                    
        