#attempt1: You could use cmp_to_key function or push ro dict and check against dict values
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        di={}
        k=len(order)
        for i in range(k):
            di[order[i]]=i
        for i in "qwertyuiopasdfghjklzxcvbnm":
            if i not in di:
                di[i]=k
                k+=1
        s=sorted(str,key=lambda x:di[x])
        return "".join(s)
        
        