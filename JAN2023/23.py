#attempt2:
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        isTrusted = [0]*(n+1)
        doesPersonTrust = set()
        for a,b in trust:
            isTrusted[b] += 1
            if a not in doesPersonTrust:
                doesPersonTrust.add(a)
        
        trustedByAll = set([index for index,num in enumerate(isTrusted) if num==n-1])
        ans = trustedByAll - doesPersonTrust
        if len(ans) != 1:
            return -1
        for ele in ans:
            return ele

#attempt1: DIdn't solve for n=1
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        isTrusted = [0]*(n+1)
        doesPersonTrust = set()
        for a,b in trust:
            isTrusted[b] += 1
            if a not in doesPersonTrust:
                doesPersonTrust.add(a)
        
        trustedByAll = set([index for index,num in enumerate(isTrusted) if num==n-1])
        ans = trustedByAll - doesPersonTrust
        if len(ans) != 1:
            return -1
        for ele in ans:
            return ele

'''
