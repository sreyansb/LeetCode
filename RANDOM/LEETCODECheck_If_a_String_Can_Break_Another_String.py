class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        s2=sorted(s2)
        n=len(s1)
        #print(s1,s2)
        flag=0
        for i in range(n):
            if s1[i]<s2[i]:
                flag=1
                break
        if flag:
            flag=0
            for i in range(n):
                if s2[i]<s1[i]:
                    flag=1
                    break
            if flag:
                return False
            return True
        return True
