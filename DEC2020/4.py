#attempt1:
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        def calfactors(n):
            s=set()
            for i in range(1,int(n**0.5)+1):
                if n%i==0:
                    s.add(i)
                    s.add(n//i)
            return sorted(s)
        j=calfactors(n)
        if len(j)<k:
            return -1
        return j[k-1]
        
